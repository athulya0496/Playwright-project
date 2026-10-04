
from playwright.sync_api import Page
import time


def test_product_name_and_price(page: Page):
    page.goto("https://www.amazon.in")
    page.locator("//input[@id='twotabsearchtextbox']").fill("spanner")
    page.locator("//input[@id='nav-search-submit-button']").click()
    product_name_tag = page.locator("//span[text()='Taparia 1171-8, 8-Inch (205 mm) Adjustable Spanner - Forged Chrome Vanadium Steel with Precision Jaws and Insulated Grip, 26mm Jaw Opening for Tightening, Loosening, and Plumbing - Professional Tool for Mechanics, Electricians, and DIY Repairs']")
    product_name = product_name_tag.inner_text()

    price = product_name_tag.locator("xpath=.//../../../../div[@class='a-section a-spacing-none a-spacing-top-small s-price-instructions-style']/div[@class='a-row a-size-base a-color-base']/div[@class='a-row']/a/span[@class='a-price']/span[@class='a-offscreen']").inner_text()

    print(product_name)
    print(price)



    # page.search("//div[@class= 'hmenu-item hmenu-title ']")
    # div = page.locator("//a[@class='a-link-normal s-line-clamp-3 s-link-style a-text-normal]").click
    # div= page.locator("//div[@class=class="a-section a-spacing-none aok-align-center aok-relative"]")
    # print(div.inner_text())

    time.sleep(2)


