import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose languages: ru, en, ... (etc.)")

@pytest.fixture
def get_chrome_options(request):
    options = chrome_options()
    options.add_argument('crome')
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return options

@pytest.fixture(scope="function")
def browser(get_chrome_options):
    options = get_chrome_options
    browser = webdriver.Chrome(options=options)
    print("\nstart Chrome browser for test...")
    yield browser

    browser.close()
    print("\nquit browser...")
    browser.quit()

