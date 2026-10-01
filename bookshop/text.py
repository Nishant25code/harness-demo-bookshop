"""Small text helpers used by the catalog and the templates."""
import re
import unicodedata


def slugify(text):
    """Turn a title into a URL slug, e.g. "The Time Machine" -> "the-time-machine".

    Slugs contain only lowercase ASCII letters, digits and single hyphens.
    """
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-")


def format_price(value):
    """Format a price in US dollars for display."""
    return f"${value}"


def truncate(text, length=80):
    """Shorten text to at most `length` characters, ending with an ellipsis."""
    if len(text) <= length:
        return text
    return text[: length - 1].rstrip() + "…"
