def test_get_options(page):
    page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
    page.locator("(//li[@class='inactive'])[1]/a").click()
    products_locators =  page.locator("//h2[@class='product-title']")
    
   
    print("num of books =" , products_locators.count())

    print("products list",products_locators.all_inner_texts())
    
    product_list =["Computing and Internet" "Fiction" "Health Book"]
    for i in product_list:
     product = page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
     product.click()
     
     print("first book is", products_locators.nth(0).all_text_contents)