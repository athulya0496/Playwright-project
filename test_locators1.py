def test_count_the_links(page):
    page.goto("https://www.amazon.in/" ,wait_until="domcontentloaded")
    links_locator = page.locator("//a")
    links_locator.first.wait_for(state="attached")
    links = links_locator.all()
    print(len(links))
    print(len(links))
    print(type(links))
    for i in links:
        print(i.text_content(),flush =True)
        print("*"* 50)
        for i in links:
            print(i.get_attribute("href"),flush=True)
    
    
