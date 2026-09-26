from bookshop.reviews import average_rating, stars
from bookshop.text import slugify, truncate


def test_slugify_simple_titles():
    assert slugify("Dracula") == "dracula"
    assert slugify("The Time Machine") == "the-time-machine"


def test_truncate_keeps_short_text():
    assert truncate("Short text", 20) == "Short text"


def test_truncate_adds_ellipsis():
    result = truncate("A very long sentence that keeps going", 12)
    assert result.endswith("…")
    assert len(result) <= 12


def test_average_rating():
    assert average_rating([{"rating": 4}, {"rating": 5}]) == 4.5


def test_stars():
    assert stars(3.6) == "★★★★☆"
