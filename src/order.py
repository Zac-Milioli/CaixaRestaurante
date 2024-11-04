"""
## Order

Classe referente ao pedido do cliente
"""
from datetime import datetime

DATE_FORMAT = "%d/%m/%Y %H:%M"

class Order:
    """
    ## Order

    Classe referente ao pedido do cliente
    ```
    weight: float = Peso do pedido (Kg)
    price: float = Valor do peso (R$/Kg)
    paid: float = Valor pago pelo cliente
    cost: float = Valor do pedido
    change: float = Troco
    date: str = Data em que foi criado (dd/mm/aa hh:mm)
    ```
    """
    def __init__(self, weight: float, price: float, paid: float):
        self._weight: float = weight
        self._price: float = price
        self._paid: float = paid
        self._cost: float = round(self._weight*self._price, 2)
        self._change: float = self._paid-self._cost
        self._date: str = datetime.strftime(datetime.now(), format=DATE_FORMAT)

    @property
    def get_change(self):
        """
        Retorna o troco
        """
        return round(self._change, 2)

    @property
    def get_price(self):
        """
        Retorna o valor (R$/Kg) do pedido
        """
        return self._price

    @property
    def get_cost(self):
        """
        Retorna o custo do pedido
        """
        return round(self._cost, 2)

    @property
    def get_weight(self):
        """
        Retorna o peso
        """
        return self._weight

    @property
    def get_paid(self):
        """
        Retorna o valor pago
        """
        return self._paid

    @property
    def get_date(self):
        """
        Retorna a data de registro do pedido
        """
        return self._date

    def to_dict(self) -> dict:
        """
        Retorna a versão em dict do objeto
        ```
        {
            "weight": float,
            "value": float,
            "paid": float,
            "cost": float,
            "change": float,
            "date": str
        }
        ```
        """
        return {
            "weight": self.get_weight,
            "value": self.get_price,
            "paid": self.get_paid,
            "cost": self.get_cost,
            "change": self.get_change,
            "date": self.get_date
        }
