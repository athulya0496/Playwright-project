import pytest
import time
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_get_options(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await async_page.locator("//a[@href='/digital-downloads']").nth(0).click()

    product_name = await async_page.locator("//span[@class='price actual-price' and text()='1.00']/../../../h2").inner_text()

    await async_page.locator("//span[@class='price actual-price' and text()='1.00']/../../div[@class='buttons']/input").click()

    time.sleep(2)
    await async_page.locator("//a[@href='/cart']").nth(0).click()

    await expect(async_page.locator(f"//tbody/tr/td/a[@class='product-name' and text() = '{product_name}']")).to_have_text(product_name)

