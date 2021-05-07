from bs4 import BeautifulSoup
from requests_cache import CachedSession
import re

url = "http://devri.bzh/dictionnaire/a/a-abadennou/"
url_2 = "http://devri.bzh/dictionnaire/a/a-adwezh/"
url_3 = "http://devri.bzh/dictionnaire/a/a-bann/"
url_4 = "http://devri.bzh/dictionnaire/a/a-bar-ma/"


def get_page_content(url):
    session = CachedSession()
    page = session.get(url, timeout=2)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.prettify()
    return content


def get_entries(url):
    entries_list = []
    session = CachedSession()
    page = session.get(url, timeout=1)
    soup = BeautifulSoup(page.content, "html.parser")

    # get entry text
    entry = soup.find_all("h1", class_="titre-mot")[0].text

    # handle different variants
    entries = soup.find_all("b")
    years = soup.find_all("i")
    if len(entries) == len(years):
        for i, j in zip(entries, years):
            entry_list = []
            year = re.findall(r"\([0-9]{4}\)", j.text)
            if year:
                year = year[0][1:5]
                entry_list.append(re.sub(r'[^A-Za-z0-9-]+', '', entry))
                entry_list.append(re.sub(r'[^A-Za-z0-9-]+', '', i.text))
                entry_list.append(year)
                entries_list.append(entry_list)
            else:
                pass
    else:
        return None
    return entries_list


res = get_entries(url_4)
print(res)
