from typing import List, Dict
from time import sleep

from models.products import Product
from utils.helper import format_float_str_coin


products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('=============================')
    print('=========Bem-Vindo(a)========')
    print('=========Personal Shop=======')
    print('=============================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_products()
    elif option == 4:
        view_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def register_product() -> None:
    print('Cadastro de produto')
    print('-------------------')

    name: str = input('Informe o nome do produto: ')
    price: float = float('Informe o preço do produto: ')

    product: Product = Product(name, price)
    products.append(product)

    print(f'O produto {product.name} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def list_products() -> None:
    if len(products) > 0:
        print('Listagem de Produtos')
        print('--------------------')
        for product in products:
            print(product)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

def buy_products() -> None:
    if len(products) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('====================Produtos Disponíveis======================')
        for product in products:
            print(product)
            print('----------------------------------------------------------')
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if product:
            if len(cart) > 0:
                have_in_cart: bool = False
                for item in cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(f'O produto {product.name} agora possui {quant + 1} unidades no carrinho')
                        have_in_cart = True
                        sleep(2)
                        menu()
                if not have_in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'O produto {product.name} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'O produto {product.name} foi adicionado ao carrinho')
                sleep(2)
                menu()

        else:
            print(f'O produto com o código {code} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Não existem produtos para vender.')

def view_cart() -> None:
    pass

def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Produtos do Carrinho: ')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantidade: {data[1]}')
                total_value += data[0].price * data[1]
                print('------------------------')
                sleep(1)
        print(f'Sua fatura é {format_float_str_coin(total_value)}')
        print('Volte Sempre!')
        cart.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def get_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p

if __name__ == '__main__':
    main()
