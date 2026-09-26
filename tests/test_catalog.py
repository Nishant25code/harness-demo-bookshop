from bookshop.catalog import find_by_slug, load_books, search, sort_books


def test_catalog_loads_all_books():
    assert len(load_books()) == 24


def test_search_by_exact_title():
    assert [book.title for book in search(load_books(), "Dracula")] == ["Dracula"]


def test_search_by_author():
    titles = {book.title for book in search(load_books(), "Jules Verne")}
    assert "Treasure Island" not in titles
    assert "Around the World in Eighty Days" in titles


def test_sort_by_title():
    titles = [book.title for book in sort_books(load_books(), "title")]
    assert titles == sorted(titles, key=str.lower)


def test_sort_by_price_low_to_high():
    prices = [book.price for book in sort_books(load_books(), "price_asc")]
    assert prices == sorted(prices)


def test_unknown_sort_falls_back_to_title():
    assert sort_books(load_books(), "nope") == sort_books(load_books(), "title")


def test_find_by_slug():
    assert find_by_slug(load_books(), "dracula").author == "Bram Stoker"
    assert find_by_slug(load_books(), "missing") is None
