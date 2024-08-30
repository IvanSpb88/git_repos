from lesson_7.Swag_Labs_v2.Pages.LoginPage import LoginPage
from lesson_7.Swag_Labs_v2.Pages.ProductsPage import ProductsPage
from lesson_7.Swag_Labs_v2.Pages.CheckoutPage import CheckoutPage

user_name = "standard_user"
password = "secret_sauce"

first_name = "Mark"
last_name = "Markov"
postal_code = "123456"

sum = "$58.29"


def test_purchase(chrome_browser):
    
    login_page = LoginPage(chrome_browser)
    login_page.open()
    login_page.sign_in(user_name, password)
    
    products_page = ProductsPage(chrome_browser)
    products_page.add_to_cart()
    products_page.go_to_cart()
    products_page.checkout_click()
    
    checkout_page = CheckoutPage(chrome_browser)
    checkout_page.make_checkout(first_name, last_name, postal_code)
    
    txt = checkout_page.check_total()
    assert sum in txt
    