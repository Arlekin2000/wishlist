from .steampay import steampay


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
