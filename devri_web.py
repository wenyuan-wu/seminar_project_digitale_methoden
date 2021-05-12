import requests.exceptions
from bs4 import BeautifulSoup
from requests_cache import CachedSession
import socket
import requests.packages.urllib3.util.connection as urllib3_cn
from tqdm import tqdm
import re
import csv
import time
import sacrebleu

"""
This script serve the purpose to perform the web scraping to the website http://devri.bzh/, where nearly entire database
of entries about historical variants will be extracted. The website data are cached in the http_cache.sqlite in order
to save time from redundant work. Without cache, the entire web scraping process should take around 4 hours. 
Things for improvement: better entry extraction strategy.
"""


def allowed_gai_family() -> socket.AF_INET:
    """
    Force request library to use ipv4, the original website doesn't support ipv6 which slows down the
    process drastically.
    :return: socket families
    """
    family = socket.AF_INET
    return family


def get_page_url():
    """
    Initial function to get the list of page urls with respect to different alphabet.
    :return: list of urls
    """
    page_url_list = []
    url = "http://devri.bzh/dictionnaire/a/"
    session = CachedSession()
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    letter_list = soup.find_all("a", class_="enfant")
    for i in tqdm(letter_list):
        url_letter = "http://devri.bzh" + i["href"]
        page_letter = session.get(url_letter)
        soup_letter = BeautifulSoup(page_letter.content, "html.parser")
        page_num = soup_letter.find("li", class_=["MarkupPagerNavLast MarkupPagerNavLastNum", "MarkupPagerNavLastNum"])
        try:
            page_num = page_num.a.text
            url_list = [url_letter]
            for j in range(2, int(page_num) + 1):
                url_list.append(url_letter + f"page{j}")
            page_url_list += url_list
        except AttributeError:
            pass
    # add page for alphabet z manually
    page_url_list += ["http://devri.bzh/dictionnaire/z/"]
    return page_url_list


def get_entry_url_list(page_url_list: list) -> list:
    """
    Function to get the url list of all entries.
    :param page_url_list: list of urls from alphabet pages
    :return: list of urls
    """
    entry_url_list = []
    for url in tqdm(page_url_list):
        url_li = get_entry_url(url)
        entry_url_list += url_li
    return entry_url_list


def get_entry(entry_url_list: list) -> list:
    """
    Function to extract entries which matches the filter.
    :param entry_url_list: list of entry urls
    :return: nested list of entries
    """
    entry_list = []
    for url in tqdm(entry_url_list):
        # handle ConnectTimeout exception for request library, probably not needed anymore
        try:
            entry = get_entry_content(url)
        except requests.exceptions.ConnectTimeout:
            print("Connection refused by the server..")
            print("Let me sleep for 10 seconds")
            print("ZZzzzz...")
            time.sleep(10)
            print("Was a nice sleep, now let me continue...")
            continue
        if entry:
            entry_list += entry
    return entry_list


def get_page_content(url: str) -> str:
    """
    Utilization function to get page content literally
    :param url: string
    :return: string
    """
    session = CachedSession()
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.prettify()
    return content


def get_entry_url(url: str) -> list:
    """
    Function to extract url of entries from alphabet page url
    :param url: string
    :return: list of urls
    """
    url_list = []
    session = CachedSession()
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    entry_url = soup.find_all("li", class_="list-group-item col-md-4")
    for i in tqdm(entry_url):
        url = "http://devri.bzh" + i.a["href"]
        url_list.append(url)
    return url_list


def get_entry_content(url: str) -> [list, None]:
    """
    Function to extract entry content given entry url
    :param url: string
    :return: list of entry contents or None type if doesn't match filters
    """
    entries_list = []
    session = CachedSession()
    page = session.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # get entry text
    entry = soup.find_all("h1", class_="titre-mot")[0].text

    # handle different variants
    # TODO: better extraction strategy
    entries = soup.find_all("b")
    years = soup.find_all("i")
    if len(entries) == len(years):
        for i, j in zip(entries, years):
            entry_list = []
            year = re.findall(r"\([0-9]{4}\)", j.text)
            if year:
                year = year[0][1:5]
                src = re.sub(r'[^A-Za-z\'-*]+', '', entry)
                trg = re.sub(r'[^A-Za-z\'-*]+', '', i.text)
                try:
                    score = get_char_bleu(src, trg)
                    if score > 10.0:
                        entry_list.append(trg)
                        entry_list.append(src)
                        entry_list.append(year)
                        # bleu score as additional information
                        # entry_list.append(score)
                        entries_list.append(entry_list)
                except EOFError:
                    pass

    return entries_list


def get_char_bleu(src: str, trg: str) -> float:
    """
    Fucntion to calculate character BLEU score
    :param src: string, source
    :param trg: string, target
    :return: float, BLEU score
    """
    src = " ".join(src)
    trg = " ".join(trg)
    return sacrebleu.sentence_bleu(src, [trg]).score


def write_to_csv(entry_list: list, file_name: str) -> None:
    """
    Function to write list of entry contents into csv file for further process
    :param entry_list: list
    :param file_name: string
    :return: None
    """
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(entry_list)


def main():
    # force requests to use ipv4
    urllib3_cn.allowed_gai_family = allowed_gai_family

    page_url_list = get_page_url()
    entry_url_list = get_entry_url_list(page_url_list)
    entry_list = get_entry(entry_url_list)
    write_to_csv(entry_list, "data/breton_devri.csv")


if __name__ == '__main__':
    main()
