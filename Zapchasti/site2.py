import requests
from curl import cookies2, headers2
from bs4 import BeautifulSoup

def site2(article):
    response = requests.get(f"https://atvgear.ru/search/?query={article}", headers=headers2, cookies=cookies2)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    price = soup.find("div", class_="p-thumbs__price").text
    name = soup.find("div", class_="p-thumbs__text-name").text

    print("Сайт: https://atvgear.ru/")
    print(f"Цена: {price}")
    print(f"Название: {name}")