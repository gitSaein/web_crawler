from urllib.request import urlopen
import bs4

url = "http://www.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")

# print(type(bs_obj))
# print(bs_obj.findAll("li")[1])
# print(bs_obj.find("div", {"id": "da_brand"}))
atag = bs_obj.find("a")
print(atag['href'])
