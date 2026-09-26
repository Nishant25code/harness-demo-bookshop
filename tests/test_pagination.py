from bookshop.pagination import paginate


def test_first_page():
    page = paginate(list(range(25)), 1, 10)
    assert page.items == list(range(10))
    assert page.has_next
    assert not page.has_prev


def test_last_partial_page():
    page = paginate(list(range(25)), 3, 10)
    assert page.items == [20, 21, 22, 23, 24]
    assert page.total_pages == 3
    assert not page.has_next
