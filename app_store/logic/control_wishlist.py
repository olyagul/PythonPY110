import json
import os
from app_store.models import DATABASE

PATH_WISHLIST = 'wishlist.json'


def view_in_wishlist(username: str = '') -> dict:
    """
    Просматривает содержимое wishlist.json
    """
    empty_user_wishlist = {'products': []}

    if os.path.exists(PATH_WISHLIST):
        with open(PATH_WISHLIST, encoding='utf-8') as f:
            wishlist = json.load(f)
            if username not in wishlist:
                wishlist[username] = empty_user_wishlist
    else:
        wishlist = {username: empty_user_wishlist}

    with open(PATH_WISHLIST, mode='w', encoding='utf-8') as f:
        json.dump(wishlist, f, ensure_ascii=False, indent=4)

    return wishlist


def add_to_wishlist(id_product: str, username: str = '') -> bool:
    """
    Добавляет продукт в избранное
    """
    wishlist = view_in_wishlist(username)

    # Проверяем существует ли товар в базе данных
    if id_product not in DATABASE:
        return False

    user_wishlist = wishlist[username]['products']

    # Добавляем товар только если его еще нет в избранном
    if id_product not in user_wishlist:
        user_wishlist.append(id_product)

        with open(PATH_WISHLIST, mode='w', encoding='utf-8') as f:
            json.dump(wishlist, f, ensure_ascii=False, indent=4)
        return True
    return False


def remove_from_wishlist(id_product: str, username: str = '') -> bool:
    """
    Удаляет продукт из избранного
    """
    wishlist = view_in_wishlist(username)

    user_wishlist = wishlist[username]['products']

    # Проверяем существует ли товар в избранном
    if id_product not in user_wishlist:
        return False

    # Удаляем товар из списка
    user_wishlist.remove(id_product)

    with open(PATH_WISHLIST, mode='w', encoding='utf-8') as f:
        json.dump(wishlist, f, ensure_ascii=False, indent=4)

    return True


if __name__ == "__main__":
    # Тестирование функций
    if os.path.exists('wishlist.json'):
        os.remove('wishlist.json')

    print('Проверяем избранное', "Ответ:     {'': {'products': []}}", f'Результат: {view_in_wishlist()}\n', sep='\n')
    print('Добавляем товар с id = 1', 'Ответ:     True', f'Результат: {add_to_wishlist("1")}\n', sep='\n')
    print('Добавляем товар с id = 0', 'Ответ:     False', f'Результат: {add_to_wishlist("0")}\n', sep='\n')
    print('Добавляем товар с id = 1 (повторно)', 'Ответ:     False', f'Результат: {add_to_wishlist("1")}\n', sep='\n')
    print('Добавляем товар с id = 2', 'Ответ:     True', f'Результат: {add_to_wishlist("2")}\n', sep='\n')
    print('Проверяем избранное', "Ответ:     {'': {'products': ['1', '2']}}", f'Результат: {view_in_wishlist()}\n', sep='\n')
    print('Удаляем товар с id = 0', "Ответ:     False", f'Результат: {remove_from_wishlist("0")}\n', sep='\n')
    print('Удаляем товар с id = 1', "Ответ:     True", f'Результат: {remove_from_wishlist("1")}\n', sep='\n')
    print('Проверяем избранное', "Ответ:     {'': {'products': ['2']}}", f'Результат: {view_in_wishlist()}\n', sep='\n')

    if os.path.exists('wishlist.json'):
        os.remove('wishlist.json')
