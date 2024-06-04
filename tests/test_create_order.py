import pytest
import requests
import json
import allure
import urls
import data


class TestCreateOrder:
    @allure.title('Создание заказа с разными цветами ')
    @pytest.mark.parametrize('colors', [
        ['BLACK'],
        ['GREY'],
        ['BLACK','GREY'],
        []
    ])
    def test_create_order_with_different_colors(self, colors):
        payload = data.CreateOrderData.order_data
        payload['color'] = colors
        payload = json.dumps(payload)
        response = requests.post(urls.ORDER, data=payload)
        assert response.status_code == 201 and 'track' in response.text

