import requests
import allure
import urls


class TestOrderList:
    @allure.title('Получение списка заказов')
    def test_get_list_orders(self):
        response = requests.get(urls.ORDER)
        assert response.status_code == 200 and len(response.json()['orders']) > 0

