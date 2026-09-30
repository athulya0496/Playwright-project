def test_table(page):
 page.goto("https://www.w3schools.com/Html/html_tables.asp")
 count_tables = page.locator("//table").count()
 print(count_tables, flush= True)
    