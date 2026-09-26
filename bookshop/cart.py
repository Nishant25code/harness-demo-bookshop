"""Shopping cart, stored in the session as {"items": {book_id: quantity}, "code": ...}."""

DISCOUNT_CODES = {
    "SAVE10": 10,
    "BOOKWORM": 15,
    "WELCOME5": 5,
}


class Cart:
    def __init__(self, items=None, code=None):
        self.items = dict(items or {})
        self.code = code

    @classmethod
    def from_session(cls, data):
        data = data or {}
        return cls(items=data.get("items"), code=data.get("code"))

    def to_session(self):
        return {"items": self.items, "code": self.code}

    def add(self, book_id, quantity=1):
        self.items[book_id] = self.items.get(book_id, 0) + quantity

    def remove(self, book_id):
        """Remove one copy of a book from the cart."""
        if book_id in self.items:
            self.items[book_id] -= 1
            if self.items[book_id] <= 0:
                del self.items[book_id]

    def count(self):
        return sum(self.items.values())

    def lines(self, books_by_id):
        """(book, quantity, line total) for every book in the cart."""
        result = []
        for book_id, quantity in self.items.items():
            book = books_by_id.get(book_id)
            if book is not None:
                result.append((book, quantity, round(book.price * quantity, 2)))
        return result

    def subtotal(self, books_by_id):
        return round(sum(line_total for _, _, line_total in self.lines(books_by_id)), 2)

    def apply_code(self, code):
        code = code.strip().upper()
        if code not in DISCOUNT_CODES:
            raise ValueError(f"Unknown discount code: {code}")
        self.code = code

    def discount(self, books_by_id):
        """Amount taken off the subtotal by the applied discount code."""
        if not self.code:
            return 0.0
        percent = DISCOUNT_CODES[self.code]
        return round(self.subtotal(books_by_id) * percent / 100, 2)

    def total(self, books_by_id):
        return round(self.subtotal(books_by_id) - self.discount(books_by_id), 2)
