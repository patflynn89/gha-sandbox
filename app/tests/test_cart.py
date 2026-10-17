import pytest

from shopcart import Cart, Item


def test_empty_cart_is_zero():
    assert Cart().total_cents() == 0


def test_subtotal_multiplies_quantity():
    cart = Cart()
    cart.add(Item("apple", 50, quantity=3))
    cart.add(Item("pear", 120))
    assert cart.subtotal_cents() == 270


def test_discount():
    cart = Cart([Item("tv", 10_000)])
    assert cart.total_cents(discount_percent=15) == 8_500


@pytest.mark.parametrize("bad", [-1, 101])
def test_invalid_discount(bad):
    with pytest.raises(ValueError):
        Cart().total_cents(discount_percent=bad)


def test_negative_price_rejected():
    with pytest.raises(ValueError):
        Item("broken", -5)
