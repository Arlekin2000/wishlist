import requests
from bs4 import BeautifulSoup


def steampay(game):
    url = "https://steampay.com/search?q=" + "+".join(game.lower().split())
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    name_games = [" ".join(i.text.split()) for i in soup.findAll("div", class_="catalog-item__name")]
    price_games = [i.text.strip() for i in soup.findAll("span", class_="catalog-item__price-span")]
    links = ["https://steampay.com" + i["href"] for i in soup.findAll("a", class_="catalog-item")]
    return [{"name":name_games[i], "price":price_games[i], "link":links[i]} for i in range(len(name_games))]


if __name__ == "__main__":
    [print(i) for i in steampay(input())]
