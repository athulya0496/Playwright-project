# page.getByLabel() to locate a form control by associated label's text.
def test_get_by_label(page):
    page.goto("https://demowebshop.tricentis.com/")
    register_link = page.get_by_text("Register")
    register_link.click()
    page.get_by_label("Female").nth(0).check()
    page.get_by_label("First name:").fill("abc")
    page.get_by_label("Last name:").fill("xyz")
    page.get_by_label("Email:").fill("abc@gmail.com")
   #page.get_by_label("Password:").fill("abc123") 
    page.get_by_label("Password:").nth(0).fill("abc123")
    
    page.get_by_label("Confirm Password:").fill("abc123")
    page.get_by_role("button", name="Register").click()