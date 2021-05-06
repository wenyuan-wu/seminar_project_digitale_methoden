from bs4 import BeautifulSoup
from requests_cache import CachedSession
import requests
from urllib.request import urlopen
import re

url = "http://devri.bzh/dictionnaire/a/a-abadennou/"
url_2 = "http://devri.bzh/dictionnaire/a/a-adwezh/"
url_3 = "http://devri.bzh/dictionnaire/a/a-aes-vat/"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")


# session = requests.session()
session = CachedSession()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
# page = session.get(url_3)
# timeout works
page = session.get(url, timeout=5)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
# print(list(soup.children))
# print(soup.prettify())

results = soup.find_all('h1', class_='titre-mot')

for i in results:
    print(i.text)

# bold
results_n = soup.find_all('b')

for i in results_n:
    print(i.text)

results_s = soup.find_all('i')
print(len(results_s))
for i in results_s:
    print(i.text)
