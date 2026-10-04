
def test_get_options(page): 
    page.goto("https://www.amazon.in")
    page.locator("//a[@id='nav-hamburger-menu']").click()
    div = page.locator("//div[contains(@class, 'hmenu-item') and contains(@class, 'hmenu-title')]")
    
    div.first.wait_for()

    count=div.count()

    for i in range(count):

        print(div.nth(i).inner_text(), flush=True)
    