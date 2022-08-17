import time
from selenium.webdriver.common.by import By


def _check_items(browser):
    """ check element """
    cnt = len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"))
    if cnt > 0:
        return True
    else:
        return False

def test_check_basket_button(browser):
    """ test items """
    link = r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    assert _check_items(browser), "Element not found"
