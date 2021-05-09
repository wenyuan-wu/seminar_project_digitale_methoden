from bs4 import BeautifulSoup
from requests_cache import CachedSession
from tqdm import tqdm
import re
import csv


def get_page_url():
    page_url_list = []
    url = "http://devri.bzh/dictionnaire/a/"
    session = CachedSession()
    page = session.get(url, timeout=2)
    soup = BeautifulSoup(page.content, "html.parser")
    letter_list = soup.find_all("a", class_="enfant")
    for i in tqdm(letter_list):
        url_letter = "http://devri.bzh" + i["href"]
        page_letter = session.get(url_letter, timeout=2)
        soup_letter = BeautifulSoup(page_letter.content, "html.parser")
        page_num = soup_letter.find("li", class_=["MarkupPagerNavLast MarkupPagerNavLastNum", "MarkupPagerNavLastNum"])
        try:
            page_num = page_num.a.text
            url_list = [url_letter]
            for j in tqdm(range(2, int(page_num) + 1)):
                url_list.append(url_letter + f"page{j}")
            page_url_list += url_list
        except AttributeError:
            pass
    page_url_list += ["http://devri.bzh/dictionnaire/z/"]
    return page_url_list


def get_entry_url_list(page_url_list):
    entry_url_list = []
    for url in tqdm(page_url_list):
        url_li = get_entry_url(url)
        entry_url_list += url_li
    return entry_url_list


def get_entry(entry_url_list):
    entry_list = []
    for url in tqdm(entry_url_list):
        entry = get_entry_content(url)
        if entry:
            entry_list += entry
    return entry_list


def get_page_content(url):
    session = CachedSession()
    page = session.get(url, timeout=2)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.prettify()
    return content


def get_entry_url(url):
    url_list = []
    session = CachedSession()
    page = session.get(url, timeout=2)
    soup = BeautifulSoup(page.content, "html.parser")

    entry_url = soup.find_all("li", class_="list-group-item col-md-4")
    for i in tqdm(entry_url):
        url = "http://devri.bzh" + i.a["href"]
        url_list.append(url)
    return url_list


def get_entry_content(url):
    entries_list = []
    session = CachedSession()
    page = session.get(url, timeout=2)
    soup = BeautifulSoup(page.content, "html.parser")

    # get entry text
    entry = soup.find_all("h1", class_="titre-mot")[0].text

    # handle different variants
    entries = soup.find_all("b")
    years = soup.find_all("i")
    if len(entries) == len(years):
        for i, j in tqdm(zip(entries, years)):
            entry_list = []
            year = re.findall(r"\([0-9]{4}\)", j.text)
            if year:
                year = year[0][1:5]
                entry_list.append(re.sub(r'[^A-Za-z0-9\'-*]+', '', entry))
                entry_list.append(re.sub(r'[^A-Za-z0-9\'-*]+', '', i.text))
                entry_list.append(year)
                entries_list.append(entry_list)
            else:
                pass
    else:
        return None
    return entries_list


def write_to_csv(entry_list, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(entry_list)


def main():
    page_url_list = get_page_url()
    entry_url_list = get_entry_url_list(page_url_list)
    entry_list = get_entry(entry_url_list)
    write_to_csv(entry_list, "data/breton_devri.csv")


if __name__ == '__main__':
    main()
