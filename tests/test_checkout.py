"""
Testes unitários para classe Checkout
"""
from datetime import datetime
from src.checkout import Checkout

DATE_FORMAT = "%d/%m/%Y %H:%M"

class TestCheckout:
    """
    Classe para testes de Checkout
    """
    def test_01_create_checkout(self):
        """
        Testa a criação de um caixa
        """
        checkout = Checkout(starting_value=10)
        now = datetime.strftime(datetime.now(), format=DATE_FORMAT)
        assert checkout.get_init_date == now
        assert checkout.get_change == 0
        assert len(checkout.get_receipt) == 0
        assert checkout.get_starting_value == 10
        assert checkout.get_balance == 0
        assert checkout.get_weight == 0

    def test_02_place_order(self):
        """
        Testa a adição de um pedido
        """
        checkout = Checkout(starting_value=10)
        response = checkout.place_order(weight=1, value=1, paid=2)
        now = datetime.strftime(datetime.now(), format=DATE_FORMAT)
        expected_dict = {
            "weight": 1,
            "value": 1,
            "paid": 2,
            "cost": 1,
            "change": 1,
            "date": now
        }
        assert response.get("message") == "OK"
        assert checkout.get_balance == 1
        assert checkout.get_weight == 1
        assert checkout.get_change == 1
        assert len(checkout.get_receipt) == 1
        assert checkout.get_receipt_as_dicts[0] == expected_dict

    def test_03_invalid_orders(self):
        """
        Testa as situações em que pedidos são bloqueados
        """
        checkout = Checkout(starting_value=10)
        response = checkout.place_order(weight=1, value=1, paid=0)
        assert response.get("message") == 'ERRO: O valor pago é menor do que o preço do pedido'
        response = checkout.place_order(weight=1, value=1, paid=1000)
        assert response.get("message") == 'ERRO: O troco é maior do que o valor disponível em caixa'
        assert checkout.get_balance == 0
        assert len(checkout.get_receipt) == 0

    def test_04_close_checkout(self):
        """
        Testa o fechamento do caixa
        """
        checkout = Checkout(starting_value=10)
        response = checkout.close_checkout()
        now = datetime.strftime(datetime.now(), format=DATE_FORMAT)
        assert response.get("close_time") == now
        assert checkout.get_close_date == now
