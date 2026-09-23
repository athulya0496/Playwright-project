from playwright.sync_api import sync_playwright,expect



with sync_playwright() as p:
   browser= p.chromium.launch(headless=True)
   page=  browser.new_page()
   page.goto("https://www.google.com/")
   print(page.title())
   browser.close()
   
   
def test_google(page,browser_name):
    page.goto("https://www.google.com/")
    print(page.title())
    print(browser_name)
    expect(page).to_have_title("Google")
    
    