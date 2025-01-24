import requests
from bs4 import BeautifulSoup
from curl import cookies, headers

def site1(article):
    response = requests.get(f"http://www.atvleader.ru/search.html?article={article}&x=0&y=0&term=0",
                            cookies=cookies, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    price = soup.find("tr", class_="even").find("td", align="right").find("nobr").text.strip().split()
    del price[-1]
    res_price = " ".join(price)

    name = soup.find("tr", class_="even").find("td", align="left").text.strip()

    print("Сайт: http://www.atvleader.ru/")
    print(f"Цена: {res_price}")
    print(f"Название: {name}")