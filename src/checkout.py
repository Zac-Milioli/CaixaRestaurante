"""
## Checkout

Classe referente ao caixa do dia no Kilo Kaloria
"""
from datetime import datetime
from .order import Order

DATE_FORMAT = "%d/%m/%Y %H:%M"

class Checkout:
    """
    ## Checkout

    Classe do caixa
    ```
    starting_value: float = Valor que o caixa foi aberto
    change: float = Somatório dos trocos dados em operação
    weight: float = Somatório dos pesos inseridos em operação
    balance: float = Balanço do dia
    init_date: str = Data e hora de abertura do caixa
    close_date: str = Data e hora de fechamento do caixa
    receipt: list = Lista contendo todos os pedidos do dia
    ```
    """
    def __init__(self, starting_value: float):
        self._starting_value: float = starting_value
        self._change: float = 0
        self._weight: float = 0
        self._balance: float = 0
        self._init_date: str = datetime.strftime(datetime.now(), format=DATE_FORMAT)
        self._close_date: str = False
        self._receipt: list = []

    @property
    def get_balance(self) -> float:
        """
        Retorna o balanço do dia
        """
        return self._balance

    @property
    def get_starting_value(self) -> float:
        """
        Retorna o valor inicial no caixa
        """
        return self._starting_value

    @property
    def get_change(self) -> float:
        """
        Retorna o somatorio dos trocos do dia
        """
        return self._change

    @property
    def get_weight(self) -> float:
        """
        Retorna o somatorio dos pesos do dia
        """
        return self._weight

    @property
    def get_init_date(self) -> str:
        """
        Retorna a data e horário de abertura do caixa
        """
        return self._init_date

    @property
    def get_close_date(self) -> str:
        """
        Retorna a data e horário de fechamento do caixa
        """
        return self._close_date

    @property
    def get_receipt(self) -> list[Order]:
        """
        Retorna a lista com os pedidos do dia
        """
        return self._receipt

    @property
    def get_receipt_as_dicts(self) -> list[dict]:
        """
        Retorna a lista com os pedidos do dia em formato dict
        
        returns
        ```
        [{
            "weight": float,
            "value": float,
            "paid": float,
            "cost": float,
            "change": float,
            "date": str
        }, ...]
        ```
        """
        orders = [order.to_dict() for order in self._receipt]
        return orders

    def place_order(self, weight: float, value: float, paid: float) -> dict:
        """
        Cria um pedido, inclui no sistema e retorna o troco
        """
        order = Order(weight=weight, price=value, paid=paid)
        if 0 > order.get_change:
            return {"message": "ERRO: O valor pago é menor do que o preço do pedido"}
        elif order.get_change > self.get_balance+self.get_starting_value:
            return {"message": "ERRO: O troco é maior do que o valor disponível em caixa"}
        self._balance += order.get_cost
        self._weight += order.get_weight
        self._change += order.get_change
        self._receipt.append(order)
        return {"message": "OK", "change": order.get_change, "price": order.get_cost}

    def close_checkout(self) -> dict:
        """
        Fecha o caixa e retorna os dados do dia
        
        returns
        ```
        {
            "start_time": str,
            "close_time": str,
            "initial_checkout_value": float,
            "balance": float,
            "total_weight": float,
            "total_change": float,
            "orders": list[dict]
        }

        orders: {
            "weight": float,
            "value": float,
            "paid": float,
            "cost": float,
            "change": float,
            "date": str
            }
        ```
        """
        self._close_date = datetime.strftime(datetime.now(), format=DATE_FORMAT)
        return {
            "start_time": self.get_init_date,
            "close_time": self.get_close_date,
            "initial_checkout_value": self.get_starting_value,
            "balance": self.get_balance,
            "total_weight": round(self.get_weight, 3),
            "total_change": self.get_change,
            "orders": self.get_receipt_as_dicts
        }
