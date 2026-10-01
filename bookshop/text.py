"""Small text helpers used by the catalog and the templates."""


def slugify(text):
    """Turn a title into a URL slug, e.g. "The Time Machine" -> "the-time-machine"."""
    return text.strip().lower().replace(" ", "-")


def format_price(value):
    """Format a price in US dollars for display."""
    return f"${value:,.2f}"


def truncate(text, length=80):
    """Shorten text to at most `length` characters, ending with an ellipsis."""
    if len(text) <= length:
        return text
    return text[: length - 1].rstrip() + "…"
