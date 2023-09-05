"""
    Script to get various central bank rates
"""

from urllib.request import urlopen

from bs4 import BeautifulSoup
from bs4.element import NavigableString


def get_rbi_rates(page_url):
    page = urlopen(page_url)
    page_text = page.read().decode("utf-8")
    # print(page_text)
    bs_obj = BeautifulSoup(page_text, "html.parser")
    for obj in bs_obj.find_all("table"):
        for tr in obj.find_all("tr"):
            for td in tr.find_all("td"):
                for cont in td.contents:
                    if type(cont) is NavigableString:
                        formatted = cont.replace("\r\n", "").replace(" ", "").replace(":", "").replace("\n", "")
                        if len(formatted) >0:
                            print(formatted)
            print("---------")



if __name__ == "__main__":
    page_url = "https://www.rbi.org.in/"
    # page_url = "http://olympus.realpython.org/profiles/aphrodite"
    get_rbi_rates(page_url)
