"""Split a list into numbered pages."""
from dataclasses import dataclass


@dataclass
class Page:
    items: list
    number: int
    total_pages: int

    @property
    def has_prev(self):
        return self.number > 1

    @property
    def has_next(self):
        return self.number < self.total_pages


def paginate(items, page=1, per_page=12):
    total_pages = (len(items) + per_page - 1) // per_page
    page = max(1, page)
    start = (page - 1) * per_page
    return Page(items=items[start : start + per_page], number=page, total_pages=total_pages)
