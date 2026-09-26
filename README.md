# Bookshop

A tiny online bookshop built with [Flask](https://flask.palletsprojects.com/). It lists classic books, lets you search the catalog, shows each book with its reviews, and keeps a shopping cart with discount codes.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

Then open http://127.0.0.1:5000.

## Run the tests

```bash
pytest
```

## Features

- Catalog of 24 books, 12 per page, sortable by title, price or year
- Search by title or author
- Book pages with star ratings and reviews
- Session-based cart (add a book, remove one copy at a time)
- Discount codes, each a percentage off the cart subtotal:

| Code | Discount |
|---|---|
| `SAVE10` | 10% off |
| `BOOKWORM` | 15% off |
| `WELCOME5` | 5% off |

## Project layout

```
app.py                  Flask app and routes
bookshop/catalog.py     Book model, loading, lookup, search and sorting
bookshop/cart.py        Shopping cart and discount codes
bookshop/pagination.py  Pagination helper
bookshop/reviews.py     Rating helpers
bookshop/text.py        slugify, price formatting, truncation
data/books.json         The catalog
templates/              Jinja templates
static/style.css        Styles
tests/                  pytest suite
```
