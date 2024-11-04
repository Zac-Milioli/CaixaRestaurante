"""
Arquivo principal para execução do caixa
"""
import os
from glob import glob
from src.checkout import Checkout

def run() -> dict:
    """
    Função para executar a interface principal do caixa
    """
    os.system('cls')
    print("\n\n\tBem vindo!")
    while True:
        print("\n\tInsira o valor atualmente em caixa para abertura\n")
        value = input("\tR$ \t")
        try:
            checkout = Checkout(starting_value=float(value))
            os.system('cls')
            break
        except (ValueError, TypeError):
            print("\n\tVALOR INVÁLIDO")

    is_open = True
    while is_open:
        print("\nCaixa")
        print("- "*30)
        print(f"\tAbertura:\t\t   {checkout.get_init_date}")
        print(f"\tClientes atendidos:\t   {len(checkout.get_receipt)}")
        print(f"\tBalanço do dia:\t\tR$ {checkout.get_balance}\n")
        print(f"\tValor em caixa:\t\tR$ {checkout.get_balance+checkout.get_starting_value}")
        print("- "*30)
        print("\n\t[1] Atender cliente\n\n\t[ENTER] Fechar caixa e gerar relatório do dia\n")
        print("- "*30)
        option = input("\n...")
        if option == '1':
            os.system('cls')
            print("\nCaixa")
            print("- "*30)
            print(f"\tAbertura:\t\t   {checkout.get_init_date}")
            print(f"\tClientes atendidos:\t   {len(checkout.get_receipt)}")
            print(f"\tBalanço do dia:\t\tR$ {checkout.get_balance}\n")
            print(f"\tValor em caixa:\t\tR$ {checkout.get_balance+checkout.get_starting_value}")
            print("- "*30)
            weight = input("\n\tInsira o peso (gramas):\t   ")
            price = input("\n\tInsira o preço (kg):\tR$ ")
            paid = input("\n\tInsira o valor pago:\tR$ ")
            try:
                response = checkout.place_order(weight=float(weight)/1000,
                                                value=float(price),
                                                paid=float(paid))
                if response.get("message") == "OK":
                    print(f"\n\n\t\tValor do pedido:\tR$ {response.get('price')}\n")
                    print(f"\t\tTroco:\t\t\tR$ {response.get('change')}\n")
                    print("- "*30)
                    input("\n\n[ENTER] Voltar ao menu\n")
                    os.system('cls')
                else:
                    print(f"\n\n{response.get('message')}")
                    print("- "*30)
                    input("\n\n[ENTER] Voltar ao menu\n")
                    os.system('cls')
            except (ValueError, TypeError):
                print("\n\nERRO: Valor inválido inserido")
                print("- "*30)
                input("\n\n[ENTER] Voltar ao menu\n")
                os.system('cls')
        else:
            break
    return checkout.close_checkout()

if __name__ == "__main__":
    report = run()
    os.system('cls')
    REPORT_STRING = "_"*60
    REPORT_STRING += "\n\nRELATÓRIO DO DIA\n"
    REPORT_STRING += "- "*30
    REPORT_STRING += (
        f'\nAbertura do caixa:\t\t {report.get("start_time")}\n'
        f'Fechamento do caixa:\t\t {report.get("close_time")}\n'
        f'\nValor inicialmente em caixa:\t\tR$ {report.get("initial_checkout_value")}\n'
        f'\n\tBalanço:\t\t\tR$ {report.get("balance")}\n'
        f'\tTroco total dado:\t\tR$ {report.get("total_change")}\n'
        f'\tPeso total vendido (kg):\t   {report.get("total_weight")}\n'
        f"\nValor em caixa no fechamento:\t\tR$ {report.get('initial_checkout_value') + report.get('balance')}\n\n"
        "PEDIDOS DO DIA\n"
        f"Quantidade: {len(report.get('orders'))}\n"
        )
    REPORT_STRING += "- "*30
    REPORT_STRING += "\n"
    for order in report.get("orders"):
        REPORT_STRING += (
            f'\tData:\t\t\t{order.get("date")}\n'
            f'\tPeso (kg):\t\t   {order.get("weight")}\n'
            f'\tPreço (kg):\t\tR$ {order.get("cost")}\n'
            f'\tValor pago:\t\tR$ {order.get("paid")}\n'
            f'\tTroco:\t\t\tR$ {order.get("change")}\n'
            )
        REPORT_STRING += "- "*30
        REPORT_STRING += "\n"
    REPORT_STRING += "\n"
    REPORT_STRING += "_"*60

    PATH = r"output/"
    reports_number = len(glob(f'{PATH}*.txt'))+1
    with open(f"{PATH}REPORT_{reports_number}", "w", encoding="utf-8") as file:
        file.write(REPORT_STRING)
    print(REPORT_STRING)
