from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def containsNumber(value):
    if True in [char.isdigit() for char in str(value)]:
        return True
    return False


def get_soup(state="nsw"):
    url = f"https://covidlive.com.au/{state}"
    uClient = urlopen(url)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, "html5lib")


def det_cases(soup, query):
    if query == "daily":
        row = soup.find(
            "table", class_="DAILY-CASES").find_all("td", class_="COL2 NEW")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "total":
        row = soup.find(
            "table", class_="DAILY-CASES").find_all("td", class_="COL3 CASES")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "seas_d":
        row = soup.find(
            "table", class_="DAILY-SOURCE-OVERSEAS").find_all("td", class_="COL4 NET")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "seas_t":
        row = soup.find(
            "table", class_="DAILY-SOURCE-OVERSEAS").find_all("td", class_="COL2 OSEAS")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data


def det_vaccines(soup, query):
    if query == "total":
        row = soup.find(
            "table", class_="DAILY-VACCINATIONS").find_all("td", class_="COL2 DOSES")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "first":
        row = soup.find(
            "table", class_="DAILY-VACCINATIONS-FIRST-DOSES").find_all("td", class_="COL2 FIRST")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "second":
        row = soup.find(
            "table", class_="DAILY-VACCINATIONS-PEOPLE").find_all("td", class_="COL2 SECOND")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "hub":
        row = soup.find(
            "table", class_="DAILY-VACCINATIONS-SOURCE").find_all("td", class_="COL2 HUB")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "care":
        row = soup.find(
            "table", class_="DAILY-VACCINATIONS-SOURCE").find_all("td", class_="COL3 CARE")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "gp":
        row = soup.find(
            "table", class_="DAILY-VACCINATIONS-SOURCE").find_all("td", class_="COL4 GP")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "pc_first":
        data = soup.find("td", class_="VACCINATIONS").text
        return data

    if query == "pc_second":
        data = soup.find("td", class_="MA").text
        return data


def det_tests(soup, query):
    if query == "daily":
        row = soup.find(
            "table", class_="DAILY-TESTS").find_all("td", class_="COL4 NET")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "total":
        row = soup.find(
            "table", class_="DAILY-TESTS").find_all("td", class_="COL2 TESTS")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data


def det_health(soup, query):
    if query == "hosp":
        row = soup.find(
            "table", class_="DAILY-HOSPITALISED").find_all("td", class_="COL2 HOSP")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "icu":
        row = soup.find(
            "table", class_="DAILY-HOSPITALISED").find_all("td", class_="COL3 ICU")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "vent":
        row = soup.find(
            "table", class_="DAILY-HOSPITALISED").find_all("td", class_="COL4 VENT")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "deaths_t":
        row = soup.find(
            "table", class_="DAILY-DEATHS").find_all("td", class_="COL2 DEATHS")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data

    if query == "deaths_d":
        row = soup.find(
            "table", class_="DAILY-DEATHS").find_all("td", class_="COL4 NET")
        data = row[0].text if containsNumber(row[0].text) else row[1].text
        return data


def time_update(soup):
    data = soup.find(
        "a", href="/last-updated")
    return data.text
