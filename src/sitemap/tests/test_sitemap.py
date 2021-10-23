import pytest
from src.sitemap import Sitemap


@pytest.mark.parametrize("content,buy_buttons,expected",[
    ("""
    <span>Add to cart<span>
    <span>Sepete Ekle<span>
    """,
    ["Sepete Ekle"],
    True),
    ("""
    <span>Add to cart<span>
    <span>Sepete Ekle<span>
    """,
    ["No match"],
    False), 
])
def test_is_product_url(content,buy_buttons, expected):
    result = Sitemap.is_product_url(content=content, buy_buttons=buy_buttons)
    assert result == expected


@pytest.mark.parametrize("address,expected",[
    ("http://google.com", 200)
])
def test_access_address_pass(address, expected):
    result = Sitemap.access_address(address=address).status_code
    assert result == expected

@pytest.mark.parametrize("address",[
    ("http://google.comusa", 200)
])
def test_access_address_fail(address):
    with pytest.raises(Exception):
        Sitemap.access_address(address=address)

