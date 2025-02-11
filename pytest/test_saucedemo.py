from playwright.sync_api import Page
import pytest


# @pytest.mark.skip_browser("chromium")
# @pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto("inventory.html")
    assert page.title() == "Swag Labs"


def test_inventory_site(page: Page):
    page.goto("inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."

# pytest --headed --base-url https://www.saucedemo.com
# pytest --headed --base-url https://www.saucedemo.com --browser=firefox
# pytest --headed --base-url https://www.saucedemo.com --tracing on
# playwright show-trace trace.zip
# pytest --headed --base-url https://www.saucedemo.com --browser-channel=chrome
# playwright codegen https://www.saucedemo.com/v1/inventory.html
