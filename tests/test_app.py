def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bookshop" in response.data
    assert b"All books" in response.data


def test_book_page(client):
    response = client.get("/books/dracula")
    assert response.status_code == 200
    assert b"Bram Stoker" in response.data


def test_unknown_book_is_404(client):
    assert client.get("/books/no-such-book").status_code == 404


def test_search_by_title(client):
    response = client.get("/search?q=Frankenstein")
    assert b"Mary Shelley" in response.data


def test_empty_cart(client):
    response = client.get("/cart")
    assert b"Your cart is empty" in response.data


def test_add_to_cart(client):
    client.post("/cart/add/b07")
    response = client.get("/cart")
    assert b"Dracula" in response.data


def test_unknown_discount_code(client):
    client.post("/cart/add/b07")
    response = client.post("/cart/code", data={"code": "FREEBOOKS"})
    assert response.status_code == 400
    assert b"Unknown discount code" in response.data
