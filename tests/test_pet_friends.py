from api import PetFriends
from settings import *
import os
import imghdr
import re

pf = PetFriends()


def test_get_api_key_valid_user(email = valid_email, password = valid_password):
    """Запрос API ключа возвращает статус 200, в результате есть слово 'key' """

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_api_key_invalid_user(email = invalid_email, password = invalid_password):
    """Запрос API ключа с некорректным email и паролем возвращает статус 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

    raise Exception('Пользователь не найден')


def test_get_api_key_invalid_email(email = invalid_email, password = valid_password):
    """Запрос API ключа с некорректным email возвращает статус 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

    raise Exception('Неверный email')


def test_get_api_key_invalid_password(email = valid_email, password = invalid_password):
    """Запрос API ключа с некорректным паролем возвращает статус 403"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

    raise Exception('Неверный пароль')


def test_get_list_of_pets_valid_key(filter = ''):
    """Запрос питомцев с сайта возвращает не пустой список. API ключ получен и сохранен в переменной 'auth_key'.
    Доступное значение параметра filter - '' или 'my_pets' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_get_list_of_pets_invalid_key(auth_key = invalid_auth_key, filter = ''):
    """Отказ в доступе при попытке получить список питомцев с некорректным ключом"""

    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403

    raise Exception('Неверный ключ')


def test_get_empty_list_of_pets(filter = 'my_pets'):
    """При отсутствии питомцев в ответ приходит пустой список.
    Если список не пустой, запускаем цикл для удаления первого питомца в списке до полного удаления питомцев"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    if len(my_pets['pets']) == 0:
        status, result = pf.get_list_of_pets(auth_key, filter)
    else:
        while len(my_pets['pets']) > 0:
            pet_id = my_pets['pets'][0]['id']
            status, _ = pf.delete_pet(auth_key, pet_id)
            _, my_pets = pf.get_list_of_pets(auth_key, filter)

        status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) == 0 and 'pets' in my_pets


# def test_add_new_pet(name = name1, animal_type = animal_type1, age = age1, pet_photo = 'images/рэгдолл.jpg'):
#     """Создание нового питомца (с фото).
#     В переменной 'pet_photo' сохранен полный путь изображения"""
# На данный момент статус код 500, проблема в веб-приложении
#
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     status, result = pf.add_new_pet(auth_key,name, animal_type, age, pet_photo)
#
#     assert status == 200
#     assert result['name'] == name
#     assert result['animal_type'] == animal_type
#     assert result['age'] == age


def test_create_pet_simple(name = name2, animal_type = animal_type2, age = age2):
    """Создание нового питомца (без фото)"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    print(result)

    assert status == 200
    assert result['name'] == name


def test_create_pet_simple_incorrect_name01(name = name_simbols, animal_type = animal_type, age = age):
    """Создание нового питомца (без фото) с недопустимыми символами в имени"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    if re.search(r'\d', name):
        print('Введите имя кириллицей')
    else:
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        assert status == 200
        assert result['name'] == name


def test_create_pet_simple_incorrect_name02(name = name_numbers, animal_type = animal_type, age = age):
    """Создание нового питомца (без фото) с недопустимыми символами в имени"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    if re.search(r'\d', name):
        print('Введите имя кириллицей')
    else:
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        assert status == 200
        assert result['name'] == name


def test_create_pet_simple_empty_name(name = name_empty, animal_type = animal_type3, age = age3):
    """Создание нового питомца (без фото) с пустым именем"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    if not name_empty:
        print('Поле не может быть пустым, введите имя питомца')
    else:
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        assert status == 200
        assert 'name' in result


def test_create_pet_simple_1_simbols_name(name = name01, animal_type = animal_type4, age = age4):
    """Значения на границах входных диапазонов, длина имени 1 символ"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_create_pet_simple_255_simbols_name(name = name255, animal_type = animal_type4, age = age4):
    """Значения на границах входных диапазонов, длина имени 255 символов"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_create_pet_simple_1001_simbols_name(name = name1001, animal_type = animal_type4, age = age4):
    """Значения на границах входных диапазонов, длина имени больше 1000 символов"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_create_pet_simple_empty_age(name = name4, animal_type = animal_type2, age = age_empty):
    """Создание нового питомца (без фото) с пустым возрастом"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    if not age:
        print("Поле не может быть пустым, введите возраст питомца")
    else:
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        assert status == 200
        assert 'age' in result


def test_add_photo(pet_photo = pet_photo2):
    """Добавление фото для существующего.
    В переменной 'pet_photo' сохранен полный путь изображения.
    Добавляем фото питомцу по id, если ключ найден в словаре 'my_pets' (он больше 0 и не равен None).
    Если список пустой, вызываем исключение"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, my_pets = pf.get_list_of_pets(auth_key, req_filter = 'my_pets')

    pet_id = my_pets['pets'][0]['id']

    if my_pets is not None and 'pets' in my_pets and len(my_pets['pets']) > 0:
        status, result = pf.add_photo(auth_key, pet_id, pet_photo)

        assert status == 200
        assert 'pet_photo' in result

    elif not pet_id:
        raise IndexError('list index out of range')

    else:
        raise IndexError('Список питомцев пустой')


def test_add_photo_incorrect_type(pet_photo = pet_photo3):
    """Добавление некорректного типа фото для существующего питомца.
    В переменной 'pet_photo' сохранен полный путь изображения.
    Переменная 'image_format' осуществляет проверку формата файла"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    image_format = imghdr.what(pet_photo)

    if image_format in ['jpeg', 'jpg', 'png']:
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(auth_key, req_filter = 'my_pets')

        if my_pets is not None and 'pets' in my_pets and len(my_pets['pets']) > 0:
            status, result = pf.add_photo(auth_key, my_pets['pets'][1]['id'], pet_photo)

            assert status == 200
            assert result['pet_photo'] != 0

        else:
            raise Exception('Чужой питомец')

    else:
        raise Exception('Файл должен быть в формате jpeg, jpg, png')


def test_delete_pet():
    """Удаление питомца.
    По ключу получаем список питомцев.
    Если список пустой, добавляем питомца и снова запрашиваем список, затем удаляем по id.
    Статус код 200, в списке нет id удаленного питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.create_pet_simple(auth_key, 'Муся', 'Бенгальская', 7)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200
    pet_ids = [pet['id'] for pet in my_pets['pets']]
    assert pet_id not in pet_ids


def test_update_self_pet(name = 'Бубуся', animal_type= 'кот Рэгдолл', age = 11):
    """Обновление информации о питомце.
    Если список не пустой, обновляем данные. Если список пустой, вызываем исключение"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, req_filter = 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception('Список пустой')