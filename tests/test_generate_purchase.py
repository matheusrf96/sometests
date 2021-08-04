

from models.purchase import Purchase
from models.holder import Holder
from models.product import Product


def payload():
    return {
        'purchase': {
            'price': 100.99,
            'payment_method': Purchase.PM_CREDITCARD,
        },
        'holder': {
            'name': 'Matheus Rodrigues',
            'document': '123.456.789-00',
            'email': 'matheus.fernandes@amopromo.com',
            'phone': '(00) 98765-4321',
        },
        'product': {
            'name': 'Produto A',
            'description': 'Produto A - Fabricante X',
        },
    }


def expected_return(payload):
    purchase_data = payload.get('purchase')
    holder_data = payload.get('holder')
    product_data = payload.get('product')

    purchase = Purchase(purchase_data.get('price'), purchase_data.get('payment_method'))
    holder = Holder(
        holder_data.get('name'), holder_data.get('document'), holder_data.get('email'), holder_data.get('phone'))
    product = Product(product_data.get('name'), product_data.get('description'))

    return purchase, holder, product


def test_generate_purchase():
    # Geral
    assert expected_return(payload()) == Purchase.generate_sale_objects(payload())

    # Quase detalhado
    expected_purchase, expected_holder, expected_product = expected_return(payload())
    purchase, holder, product = Purchase.generate_sale_objects(payload())

    assert expected_purchase == purchase
    assert expected_holder == holder
    assert expected_product == product

    # Detalhado
    assert expected_purchase.__dict__ == purchase.__dict__
    assert expected_holder.__dict__ == holder.__dict__
    assert expected_product.__dict__ == product.__dict__
