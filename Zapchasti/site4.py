import requests
from bs4 import BeautifulSoup
from curl import cookies4, headers4

def site4(article):
    response = requests.get(f"https://yamahatula.ru/catalog/?q={article}&s=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8",
                            headers=headers4, cookies=cookies4)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    price = soup.find("div", class_="price").text.strip()
    name = soup.find("div", class_="item-title").text.strip()

    print("Сайт: https://yamahatula.ru/index.php")
    print(f"Цена: {price}")
    print(f"Название: {name}")