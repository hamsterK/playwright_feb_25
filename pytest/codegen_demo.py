import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/inventory.html")
    page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click()
    page.get_by_role("link", name="1").click()
    page.pause()  # for debug
    page.get_by_role("button", name="REMOVE").click()
    expect(page).to_have_url("https://www.saucedemo.com/v1/cart.html")

# playwright codegen https://www.saucedemo.com/v1/inventory.html
# playwright codegen --device="iPhone 13" saucedemo.com
# playwright codegen --viewport-size=500,500 saucedemo.com
# playwright codegen --color-scheme=dark twitter.com
# playwright codegen --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" maps.google.com

