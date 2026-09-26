import pytest

from bookshop.cart import Cart
from bookshop.catalog import Book

BOOKS = {
    "a": Book(id="a", title="Book A", author="Author A", genre="classic", price=10.0, year=1900),
    "b": Book(id="b", title="Book B", author="Author B", genre="classic", price=4.5, year=1901),
}


def test_add_increments_quantity():
    cart = Cart()
    cart.add("a")
    cart.add("a")
    assert cart.items == {"a": 2}
    assert cart.count() == 2


def test_subtotal():
    cart = Cart({"a": 2, "b": 1})
    assert cart.subtotal(BOOKS) == 24.5


def test_remove_one_copy():
    cart = Cart({"a": 2})
    cart.remove("a")
    assert cart.items == {"a": 1}


def test_codes_are_case_insensitive():
    cart = Cart()
    cart.apply_code(" save10 ")
    assert cart.code == "SAVE10"


def test_unknown_code_is_rejected():
    with pytest.raises(ValueError):
        Cart().apply_code("FREEBOOKS")


def test_session_round_trip():
    cart = Cart({"a": 1}, code="SAVE10")
    restored = Cart.from_session(cart.to_session())
    assert restored.items == {"a": 1}
    assert restored.code == "SAVE10"
