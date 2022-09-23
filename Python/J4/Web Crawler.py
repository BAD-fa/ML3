import requests
from bs4 import BeautifulSoup


url = "https://www.w3schools.com/python/python_regex.asp"

html_content = requests.get(url).content

soup = BeautifulSoup(html_content, "html.parser")

list_of_all_links = soup.find_all("a")

with open("links.txt", "w") as f:
    for link in list_of_all_links:
        url: str = link.get("href")
        if url:
            if url.startswith("https"):
                f.write(link.get("href"))
            else:
                f.write("https://www.w3schools.com/" + link.get("href"))
        f.write("\n")
