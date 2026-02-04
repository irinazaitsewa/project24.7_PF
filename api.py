import json

import requests


class PetFriends:

    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'


    def get_api_key(self, email: str, password: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус и результат запроса в формате JSON
        с уникальным ключом пользователя, найденного по указанным email и паролю"""

        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url + 'api/key', headers = headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def get_list_of_pets(self, auth_key: json, req_filter: str = '') -> json:
        """Метод делает запрос к API сервера и возвращает статус и результат запроса в формате JSON
        со списком найденных питомцев, совпадающих с фильтром"""

        headers = {'auth_key': auth_key['key']}
        request_filter = {'filter': req_filter}

        res = requests.get(self.base_url + 'api/pets', headers = headers, params = request_filter)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: int, pet_photo: str) -> json:
        """Метод отправляет на сервер данные о добавляемом питомце (с фото)
        и возвращает статус и результат запроса в формате JSON с добавленными данными"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }

        headers = {'auth_key': auth_key['key']}

        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')}

        res = requests.post(self.base_url + 'api/pets', headers = headers, data = data, files = file)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def create_pet_simple(self, auth_key: json, name: str, animal_type: str, age: int) -> json:
        """Метод отправляет на сервер данные о добавляемом питомце (без фото)
        и возвращает статус запроса и результат в формате JSON с добавленными данными"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers = headers, data = data)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def add_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет запрос на сервер о добавлении фото питомца по ID
        и возвращает статус и результат запроса в формате JSON с обновленными данными питомца"""

        headers = {'auth_key': auth_key['key']}

        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers = headers, files = file)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по ID
        и возвращает статус и результат запроса в формате JSON с текстом уведомления об успешном удалении"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers = headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def update_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:
        """Метод отправляет на сервер запрос об обновлении данных питомца по ID
        и возвращает статус и результат запроса в формате JSON с обновленными данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers = headers, data = data)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result