import pytest
import requests
import allure
import data
import urls

class TestAuthCourier:
    @allure.title('Авторизация курьера и проверка id')
    def test_auth_courier(self):
        payload = data.Courier.data_login_password_pass
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', data=payload)
        assert response.status_code == 200 and 'id' in response.text > "0"

    @allure.title('Авторизация курьера с неверными логин/пароль')
    @pytest.mark.parametrize('creds', [
        data.Courier.data_login_pass_password_fail,
        data.Courier.data_login_fail_password_pass,
    ])
    def test_auth_courier_invalid_login_pass(self, creds):
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', data=creds)
        assert response.status_code == 404 and response.json()['message'] == data.ErrorMessage.ACCOUNT_NOT_FOUND

    @allure.title('Авторизация курьера с пустыми логин/пароль')
    @pytest.mark.parametrize('creds', [
        data.Courier.data_without_login,
        data.Courier.data_without_password,
    ])
    def test_auth_courier_invalid_login_pass(self, creds):
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', data=creds)
        assert response.status_code == 400 and response.json()['message'] == data.ErrorMessage.NOT_ENOUGH_DATA_FOR_AUTH

