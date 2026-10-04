from playwright.sync_api import Page


def test_product_name_and_rating(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("//a[@href='/books']").nth(0).click()
    product_name = "Computing and Internet"
    product_rating_style = page.locator("//a[@href='/computing-and-internet']/../../div[@class='product-rating-box']/div[@class='rating']/div").get_attribute("style")

    rating = product_rating_style.split(":")[1].strip().replace(";", "")

    print(rating)
    

    
    


