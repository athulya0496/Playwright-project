def test_locator(page):
   
 page.goto("https://demowebshop.tricentis.com/")
 page.get_by_role("link",name="Log in").click()
 page.get_by_role("textbox",name="Email").fill("abc@gmail.com")
 page.get_by_role("textbox",name="Password").fill("test@123")
 page.get_by_role("button",name= "Log in").click()
 
 
