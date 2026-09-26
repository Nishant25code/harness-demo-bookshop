"""The book catalog: loading, lookup, search and sorting."""
import json
from dataclasses import dataclass, field
from pathlib import Path

from .text import slugify

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "books.json"


@dataclass
class Book:
    id: str
    title: str
    author: str
    genre: str
    price: float
    year: int
    reviews: list = field(default_factory=list)

    @property
    def slug(self):
        return slugify(self.title)


def load_books(path=DATA_FILE):
    with open(path, encoding="utf-8") as fh:
        return [Book(**item) for item in json.load(fh)]


def find_by_slug(books, slug):
    return next((book for book in books if book.slug == slug), None)


def search(books, query):
    """Books whose title or author contains the query (case-insensitive)."""
    query = query.lower()
    return [
        book
        for book in books
        if query in book.title.lower() or query in book.author.lower()
    ]


SORT_OPTIONS = {
    # name: (key function, reverse)
    "title": (lambda book: book.title.lower(), False),
    "price_asc": (lambda book: book.price, False),
    "price_desc": (lambda book: book.price, True),
    "year": (lambda book: book.year, False),
}


def sort_books(books, sort="title"):
    key, reverse = SORT_OPTIONS.get(sort, SORT_OPTIONS["title"])
    return sorted(books, key=key, reverse=reverse)
