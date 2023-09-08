"""
    Script to get various central bank rates
"""
import logging

from urllib.request import urlopen

from bs4 import BeautifulSoup
from bs4.element import NavigableString


class CentralBankRBI:
    page_url = "https://www.rbi.org.in/"
    bank_rates = ['PolicyRepoRate', 'StandingDepositFacilityRate', 'MarginalStandingFacilityRate', 'BankRate',
                  'FixedReverseRepoRate', ]

    def __init__(self):
        pass

    def get_rbi_tables_rows(self) -> list[list]:
        """
            Get rows of all tables from RBI main page which have at least two columns
        """
        page = urlopen(self.page_url)
        page_text = page.read().decode("utf-8")
        bs_obj = BeautifulSoup(page_text, "html.parser")
        tables_rows = []

        for obj in bs_obj.find_all("table"):
            for tr in obj.find_all("tr"):
                alist = []
                for td in tr.find_all("td"):
                    for cont in td.contents:
                        if type(cont) is NavigableString:
                            formatted = cont.replace("\r\n", "").replace(" ", "").replace(":", "").replace("\n", "")

                            if len(formatted) > 0:
                                alist.append(formatted)
                                logging.debug(formatted)
                logging.debug(alist)
                if len(alist) == 2:
                    tables_rows.append(alist)
                logging.debug("------------------")
        logging.debug(tables_rows)
        return tables_rows

    def get_rbi_rates(self, tables_rows: list[list]) -> list:
        """
            Get different types of RBI rates
        """
        rates_list = []
        for name, rate in tables_rows:
            if name in self.bank_rates:
                logging.debug(rate)
                rate = float(rate.replace('%', ""))
                logging.debug(rate)
                rates_list.append([name, rate])
        logging.debug(rates_list)
        return rates_list


if __name__ == "__main__":
    bank = CentralBankRBI()
    tables_rows = bank.get_rbi_tables_rows()
    print(tables_rows)
    rates_list = bank.get_rbi_rates(tables_rows)
    print(rates_list)
