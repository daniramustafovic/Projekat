from itertools import product
from pages.home_page import HomePage

def test_login(driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_title_text() == "PRODUCTS"
    a = home_page.products(2,4)
    assert home_page.get_title_text() == "YOUR CART"
    assert home_page.provjera() == a
    home_page.checkout("Standard","User","71240")
    assert home_page.get_title_text() == "CHECKOUT: OVERVIEW"
    assert home_page.provjera() == a
    home_page.kraj()
    
    
