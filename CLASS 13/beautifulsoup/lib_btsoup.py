import requests
from bs4 import BeautifulSoup

# 1) fetch a page
resp = requests.get("https://sevreeducation.netlify.app/")
html = resp.text

# 2) parse into a soup
soup = BeautifulSoup(html, "html.parser")

# 3) print all div that has a class course
for div in soup.select("div.course"):
    print(div.get_text().strip())

# 4) Extract all links
courses = [a["href"] for a in soup.find_all("a", href=True)]
print(courses)