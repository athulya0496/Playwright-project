def test_get_by_placeholder(page):
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("books")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    


from playwright.sync_api import sync_playwright, expect
def test_get_by_alt_text(page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()
# page.getByTitle() to locate an element by its title attribute.

def test_get_by_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    #xpect(logo).to_be_visible()