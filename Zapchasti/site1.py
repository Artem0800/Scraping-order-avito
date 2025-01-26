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

    txt = ""
    for i in soup.find_all("tr", style="background: #FFE7CE; font-weight: bold"):
        name = i.find("td", align="left").text.strip()
        price = i.find("td", align="right").text.strip()
        txt += name + " | " + price + "\n"

    print("Сайт: http://www.atvleader.ru/")
    print(txt.strip())