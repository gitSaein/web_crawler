import bs4
from urllib.request import urlopen

url = "https://www.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
top_right = bs_obj.find("div", {"class": "service_area"})
first_a = top_right.find("a")
print(first_a.text)