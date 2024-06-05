import random
import string
import allure


class Delivery:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


    @staticmethod
    @allure.step('Генерация данных для регистрации курьера')
    def generation_data_for_registration(password=False):
        login = Delivery.generate_random_string(10)
        password = Delivery.generate_random_string(10)
        first_name = Delivery.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

