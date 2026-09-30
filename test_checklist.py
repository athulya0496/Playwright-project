from playwright.async_api import expect
import pytest
@pytest.mark.asyncio
async def test_check_box(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    check_box = async_page.locator("#sunday")
    await expect(check_box).not_to_be_checked()
    await check_box.check()
    await expect(check_box).to_be_checked()
    
@pytest.mark.asyncio
async def test_redio_button(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    radio_buttons = await async_page.locator("//label[text()='Gender:']/..//input[@class='form-check-input']").all()
    for readio in radio_buttons:
        await readio.click()
        expect(readio).to_be_checked()
