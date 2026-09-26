"""Small text helpers used by the catalog and the templates."""


def slugify(text):
    """Turn a title into a URL slug, e.g. "The Time Machine" -> "the-time-machine"."""
    import re
    import unicodedata
    # Convert to lowercase
    text = text.lower()
    # Normalize to decomposed form to separate characters and diacritics
    text = unicodedata.normalize('NFD', text)
    # Remove diacritics (combining characters)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Keep only letters, digits, spaces, and hyphens
    text = re.sub(r'[^a-z0-9 -]', '', text)
    # Replace sequences of spaces or hyphens with a single hyphen
    text = re.sub(r'[ -]+', '-', text)
    # Remove leading and trailing hyphens
    return text.strip('-')


def format_price(value):
    """Format a price in US dollars for display."""
    return f"${value:,.2f}"


def truncate(text, length=80):
    """Shorten text to at most `length` characters, ending with an ellipsis."""
    if len(text) <= length:
        return text
    return text[: length - 1].rstrip() + "…"
