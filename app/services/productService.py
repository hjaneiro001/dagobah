from app.entities.enums.currency import Currency
from app.entities.product import Product
from app.exceptions.productNotFoundException import ProductNotFoundException


class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_all(self):
        return self.product_repository.get_all()

    def get_id(self, id):
        product: Product = self.product_repository.get_id(id)
        if product is None:
            raise ProductNotFoundException
        return product




