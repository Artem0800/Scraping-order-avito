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

    price = ""
    for i, j in zip(soup.find_all("div", class_="p-thumbs__price"), soup.find_all("div", class_="p-thumbs__text-name")):
        price += j.text + " | " + i.text + "\n"

    print("Сайт: https://atvgear.ru/")
    print(f"{price.strip()}")