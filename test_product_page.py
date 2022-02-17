import pytest
from .page_objects.product_page import ProductPage


@pytest.mark.parametrize('offer_num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),
                                       "8", "9"])
def test_guest_can_add_product_with_promo(browser, offer_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_product_in_success_message_same()
    page.is_price_in_success_message_same()
