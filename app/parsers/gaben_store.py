import requests
from bs4 import BeautifulSoup


def gaben_store(game):
    url = "https://gabestore.ru/result?ProductFilter%5Bsearch%5D=" + "+".join(game.lower().split())
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    name = [i.text for i in soup.findAll("a", class_="shop-item__name")]
    links = ["https://gabestore.ru" + i["href"] for i in soup.findAll("a", class_="shop-item__image")]
    availability = [" ".join(i.text.split()) for i in soup.findAll("a", class_="btn btn--primary js-addToCart")] + \
                   [i.text for i in soup.findAll("a", class_="btn btn--primary btn--empty-item js-addToCart added")]
    price = [i.text for i in soup.findAll("div", class_="shop-item__price-current")]
    return [{"name": name[i], "price": price[i], "link": links[i]} for i in range(len(name)) if availability[i] == 'В корзину']


if __name__ == "__main__":
    [print(i) for i in gaben_store(input())]
