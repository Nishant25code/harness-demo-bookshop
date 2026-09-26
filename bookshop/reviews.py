"""Helpers for book reviews."""


def average_rating(reviews):
    """Average star rating of the reviews, rounded to one decimal place."""
    if not reviews:
        return 0.0
    total = sum(review["rating"] for review in reviews)
    return round(total / len(reviews), 1)


def stars(rating):
    """Render a rating out of five as stars, e.g. 3.6 -> "★★★★☆"."""
    full = int(round(rating))
    return "★" * full + "☆" * (5 - full)
