from .steampay import steampay
from .gaben_store import gaben_store


async def test_steampay(response, fixture):
    response.return_value = fixture("steampay_response.html")

    res = steampay("mafia")
    assert res

    assert res == [
        {
            'name': 'Mafia: Trilogy Экшены, Приключения',
            'price': '2385 ₽',
            'link': 'https://steampay.com/game/mafia-trilogy'
        },
        {
            'name': 'Mafia II: Definitive Edition Экшены, Приключения',
            'price': '789 ₽',
            'link': 'https://steampay.com/game/mafia-ii-definitive-edition'
        },
        {
            'name': 'Mafia III: Definitive Edition Экшены, Приключения',
            'price': '845 ₽',
            'link': 'https://steampay.com/game/mafia-iii-definitive-edition'
        },
        {
            'name': 'Doodle Mafia Симуляторы, Казуальные',
            'price': '95 ₽',
            'link': 'https://steampay.com/game/doodle-mafia'
        }
    ]


async def test_gabestore(response, fixture):
    response.return_value = fixture("gabe_store_response.html")

    res = gaben_store("mafia")
    assert res

    assert res == [
        {
            'name': 'Mafia – Definitive Edition',
            'price': '1999 ₽',
            'link': 'https://gabestore.ru/game/mafia-definitive-edition'
        },
        {
            'name': 'Mafia II – Definitive Edition',
            'price': '1299 ₽',
            'link': 'https://gabestore.ru/game/mafia-ii-definitive-edition'
        },
        {
            'name': 'Mafia III – Definitive Edition',
            'price': '1499 ₽',
            'link': 'https://gabestore.ru/game/mafia-iii-definitive-edition'
        }
    ]

