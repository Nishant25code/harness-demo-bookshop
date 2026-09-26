"""A tiny bookshop website."""
import os

from flask import Flask, abort, redirect, render_template, request, session, url_for

from bookshop.cart import Cart
from bookshop.catalog import find_by_slug, load_books, search, sort_books
from bookshop.pagination import paginate
from bookshop.reviews import average_rating, stars
from bookshop.text import format_price

PER_PAGE = 12


def create_app(books=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")

    catalog = books if books is not None else load_books()
    books_by_id = {book.id: book for book in catalog}

    app.jinja_env.filters["price"] = format_price
    app.jinja_env.globals["stars"] = stars

    def current_cart():
        return Cart.from_session(session.get("cart"))

    def save_cart(cart):
        session["cart"] = cart.to_session()

    def render_cart(cart, error=None):
        return render_template(
            "cart.html",
            cart=cart,
            lines=cart.lines(books_by_id),
            subtotal=cart.subtotal(books_by_id),
            discount=cart.discount(books_by_id),
            total=cart.total(books_by_id),
            error=error,
        )

    @app.route("/")
    def index():
        sort = request.args.get("sort", "title")
        genre = request.args.get("genre")
        page_number = request.args.get("page", 1, type=int)
        if genre:
            filtered_catalog = [book for book in catalog if book.genre.lower() == genre.lower()]
            books_to_sort = filtered_catalog
        else:
            books_to_sort = catalog
        page = paginate(sort_books(books_to_sort, sort), page_number, PER_PAGE)
        return render_template("index.html", page=page, sort=sort, genre=genre)

    @app.route("/books/<slug>")
    def book_detail(slug):
        book = find_by_slug(catalog, slug)
        if book is None:
            abort(404)
        return render_template("book.html", book=book, rating=average_rating(book.reviews))

    @app.route("/search")
    def search_page():
        query = request.args.get("q", "")
        results = search(catalog, query) if query else []
        return render_template("search.html", query=query, results=results)

    @app.route("/cart")
    def cart_page():
        return render_cart(current_cart())

    @app.post("/cart/add/<book_id>")
    def cart_add(book_id):
        if book_id not in books_by_id:
            abort(404)
        cart = current_cart()
        cart.add(book_id)
        save_cart(cart)
        return redirect(url_for("cart_page"))

    @app.post("/cart/remove/<book_id>")
    def cart_remove(book_id):
        cart = current_cart()
        cart.remove(book_id)
        save_cart(cart)
        return redirect(url_for("cart_page"))

    @app.post("/cart/code")
    def cart_code():
        cart = current_cart()
        try:
            cart.apply_code(request.form.get("code", ""))
        except ValueError as exc:
            return render_cart(cart, error=str(exc)), 400
        save_cart(cart)
        return redirect(url_for("cart_page"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
