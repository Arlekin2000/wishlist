from bs4 import BeautifulSoup
from selenium import webdriver
import time


def steambuy(game):
    driver = webdriver.Chrome()

    driver.get("https://steambuy.com/catalog/?q=" + "%20".join(game.lower().split()))
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 5500)")
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "lxml")
    name = [i.text for i in soup.findAll("div", class_="product-item__title")]
    price = [i.text for i in soup.findAll("div", class_="product-item__cost")]
    availability = [i.text for i in soup.findAll("div", class_="product-item__action")]
    links = ["https://steambuy.com" + i["href"] for i in soup.findAll("a", class_="product-item__title-link")]

    return [{"name": name[i], "price": price[i] + " " + availability[i], "link": links[i]} for i in range(len(name))]


#[print(i) for i in steambuy(input())]