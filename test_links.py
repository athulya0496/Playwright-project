def test_collecting_all_links(page):
    page.goto("https://www.flipkart.com/", wait_until="domcontentloaded")
    links = page.locator("//a")
    for i in links.all():
        print("link", i.get_attribute("href"), flush=True)

    #links.last.click()
    #links.first.click()
    links.nth(3).click()