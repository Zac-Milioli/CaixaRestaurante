"""
Testes unitários para classe Order
"""
from datetime import datetime
from src.order import Order

DATE_FORMAT = "%d/%m/%Y %H:%M"
order = Order(weight=1, price=1, paid=1)
now = datetime.strftime(datetime.now(), format=DATE_FORMAT)
expected_dict = {
    "weight": 1,
    "value": 1,
    "paid": 1,
    "cost": 1,
    "change": 0,
    "date": now
}

class TestOrder:
    """
    Classe para testes de Order
    """

    def test_01_create_order(self):
        """
        Testa a criação de um order
        """
        assert order.get_paid == 1
        assert order.get_weight == 1
        assert order.get_price == 1
        assert order.get_cost == 1
        assert order.get_change == 0
        assert order.get_date == now

    def test_02_to_dict(self):
        """
        Testa a conversão para dict
        """
        assert order.to_dict() == expected_dict
