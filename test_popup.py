from playwright.async_api import expect
import pytest

async def handle_alerts(dialog):
    print("alert type = ", dialog.type)
    print("alert msg", dialog.message)
    await dialog.accept()
    
@pytest.mark.asyncio
async def test_alerts(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    async_page.on("dialog", handle_alerts)
    await async_page.locator("//input[@type='submit']").click()
    # # await page.locator("//input[@type='submit']").click()

    await async_page.locator("#small-searchterms").fill("abc")


    
@pytest.mark.asyncio
async def test_confirm_alert(page):
    await page.goto("https://testautomationpractice.blogspot.com/")
    await page.locator("#promptBtn").click()
    # def handle_confirm_prompt(dialog):
        

    # async_page.on("dialog", lambda dialog: handle_confirm_prompt(dialog))
    # msg = async_page.locator("#demo")
    # print(msg.inner_text())
    # expect(msg).to_contain_text("Hello Abc! How are you today?")