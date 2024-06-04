import pytest
import requests
import allure
import urls
import data
from helpers import Delivery


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_create_courier_pass(self):
        payload = Delivery.generation_data_for_registration()
        response_text = '{"ok":true}'
        response = requests.post(f'{urls.CREATE_COURIER}', data=payload)
        assert response.status_code == 201 and response_text == response_text

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_courier_double(self):
        payload = Delivery.generation_data_for_registration()
        response_1 = requests.post(f'{urls.CREATE_COURIER}', data=payload)
        response_2 = requests.post(f'{urls.CREATE_COURIER}', data=payload)
        assert response_2.status_code == 409 and response_2.json()['message'] == data.ErrorMessage.LOGIN_IS_BUSY

    @allure.title('Создание курьера без одного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_field(self, field):
        payload = Delivery.generation_data_for_registration()
        del payload[field]
        response = requests.post(f'{urls.CREATE_COURIER}', data=payload)
        assert response.status_code == 400 and response.json()['message'] == data.ErrorMessage.NOT_ENOUGH_DATA_TO_REGISTER


