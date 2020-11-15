import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
bs_obs = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obs.find("ul", {"class": "list_nav"})
if ul is not None:
    lis = ul.findAll("li")
    print(lis)
    for li in ul:
        print(li)
else:
    print(None)