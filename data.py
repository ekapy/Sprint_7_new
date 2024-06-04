class ErrorMessage:
    LOGIN_IS_BUSY = 'Этот логин уже используется. Попробуйте другой.'
    NOT_ENOUGH_DATA_TO_REGISTER = 'Недостаточно данных для создания учетной записи'
    NOT_ENOUGH_DATA_FOR_AUTH = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'


class Courier:
    data_login_password_pass = {
        'login': 'zzzyoysnim',
        'password': 'khtlubzkzj'
    }
    data_login_pass_password_fail = {
        'login': 'zzzyoysnim',
        'password': 'nottestkatepassword'
    }
    data_login_fail_password_pass = {
        'login': 'nottestkatelogin',
        'password': 'khtlubzkzj'
    }
    data_without_login = {
        'login': '',
        'password': 'khtlubzkzj'
    }
    data_without_password = {
        'login': 'testkatelogin',
        'password': ''
    }


class CreateOrderData:
    order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
    }
