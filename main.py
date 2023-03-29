from shop import Shop
from store import Store
from requests import Request
from exceptions import RequestError, LogisticError

store = Store(
    items={
        'печенька': 25,
        'ноутбук': 25,
        'подушка': 10,
        'рюкзак': 10,
        'кровать': 5,
    }
)


shop = Shop(
    items={
        'печенька': 5,
        'ноутбук': 5,
        'подушка': 2,
        'рюкзак': 2,
        'рюкзак1': 2,
    }
)

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    while True:
        user_input = input(
            'Добрый день, введите ваш запрос в формате: Доставить "количество" "наименование" из "откуда" в "куда"\n'
            'Если хотите закончить нажмите: "стоп" или "stop"\n'
        ).lower()

        if user_input in ["стоп", "stop"]:
            break

        try:
            user_request = Request(user_input, storages)
        except RequestError as error:
            print(error.message)
            continue

        try:
            storages[user_request.departure].remove(user_request.product, user_request.amount)
            print(f"Нужное количество есть на {user_request.departure}")
            print(f"Курьер забрал {user_request.amount} {user_request.product} из {user_request.departure}")
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[user_request.destination].add(user_request.product, user_request.amount)
            print(f"Курьер доставил {user_request.amount} {user_request.product} в {user_request.destination}")
        except LogisticError as error:
            print(error.message)
            storages[user_request.departure].add(user_request.product, user_request.amount)
            print(f"Курьер вернул {user_request.amount} {user_request.product} в {user_request.departure}")
            continue

        for storage_name in storages:
            print(f"Сейчас в {storage_name} хранится:")
            for item, value in storages[storage_name].get_items().items():
                print(f"{item}: {value}")

        print()


if __name__ == '__main__':
    main()
