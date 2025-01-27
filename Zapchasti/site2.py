import requests
from curl import cookies2, headers2
from bs4 import BeautifulSoup

def site2(article):
    response = requests.get(f"https://atvstyle.ru/search/?q={article}", headers=headers2, cookies=cookies2)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    res = ""
    for i in soup.find_all("div", class_="prod-card__inner"):
        nal = i.find("span", class_="prod-card__labels").text.strip()
        if "В наличии" not in nal:
            continue
        name = i.find("a", class_="prod-card__name").text.strip()
        price = i.find("span", class_="prod-card__price__new").text.strip()

        res += name + " | " + price + "\n"

    print("Сайт: https://atvstyle.ru/")
    print(f"{res.strip()}")