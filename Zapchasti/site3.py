import requests
from bs4 import BeautifulSoup
from curl import headers3, cookies3

def site3(article):
    response = requests.get(f"https://atv-parts.ru/products?keyword={article}", headers=headers3, cookies=cookies3)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    price = soup.find("div", class_="product clearfix").find("span", class_="price").find("span", class_="cost").text + " р."
    name = soup.find("div", class_="product clearfix").find("a", class_="zoom").find("img").get("alt")

    print("Сайт: https://atv-parts.ru/")
    print(f"Цена: {price}")
    print(f"Название: {name}")