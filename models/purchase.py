
from models.holder import Holder
from models.product import Product


class Purchase:
    PM_CREDITCARD = 0
    PM_TRANSFER = 1

    price = 0.0
    payment_method = 0

    def __init__(self, price, payment_method):
        self.price = price
        self.payment_method = payment_method

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def generate_sale_objects(data):
        purchase_data = data.get('purchase')
        holder_data = data.get('holder')
        product_data = data.get('product')

        purchase = Purchase(purchase_data.get('price'), purchase_data.get('payment_method'))
        holder = Holder(
            holder_data.get('name'), holder_data.get('document'), holder_data.get('email'), holder_data.get('phone'))
        product = Product(product_data.get('name'), product_data.get('description'))

        return purchase, holder, product
