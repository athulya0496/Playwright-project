# load the .env file
from dotenv import load_dotenv
import os
load_dotenv()

def test_navigate(page):
   page.goto(os.getenv("BASE_URL"))