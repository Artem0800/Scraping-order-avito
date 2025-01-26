from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

def site5(article):
    driver.get(f"https://www.technomarin.ru/index.php?route=product/search&search={article}")

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    price = ""
    for i, j, h in zip(soup.find_all("span", class_="general-price"), soup.find_all("div", class_="tm-product-name-container")
                       , soup.find_all("span", class_="goods-not-available")):
        price += j.text.strip() + " | " + i.text.strip() + " | " + h.text.strip() + "\n"

    print("Сайт: https://www.technomarin.ru/")
    print(f"{price.strip()}")