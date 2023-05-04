from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
page = 1

url = "https://www.chitai-gorod.ru/search?phrase=python&page="
wb = Workbook()
ws = wb.active
ws.append(["Название", "Автор", "Цена старая", "Цена новая"])

while True:
    response = requests.get(url + str(page))
    soup = BeautifulSoup(response.text, "html.parser")

    list = soup.find_all("article")

    if(len(list)):
        for card in list:
            title = card.find("div", class_="product-title__head").text.strip()
            author_elem = card.find("div", class_="product-title__author")
            author = author_elem.text.strip() if author_elem else ""
            price_old_elem = card.find("div", class_="product-price__old")
            price_old = price_old_elem.text.strip() if price_old_elem else ""
            price_new_elem = card.find("div", class_="product-price__value product-price__value--discount")
            price_new = price_new_elem.text.strip() if price_new_elem else ""
            ws.append([title, author, price_old, price_new])
        page += 1
    else:
        break

wb.save("books.xlsx")
