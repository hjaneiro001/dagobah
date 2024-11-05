

from app.entities.enums.status import Status
from app.entities.product import Product
from app.exceptions.productAlreadyExistException import ProductAlreadyExistsException
from app.exceptions.productCodeAlreadyExistException import ProductCodeAlreadyExistsException
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

    def get_code(self, code):
        product: Product = self.product_repository.find_by_code(code)
        if product is None:
            raise ProductNotFoundException
        return product


    def create(self, product: Product):

        if self.product_repository.find_by_code(product.code):
            raise ProductAlreadyExistsException
        product.status = Status.get_status('ACTIVE')

        product_id: int = self.product_repository.create(product)
        return product_id

    def modify(self,id: int,product: Product):

        product_to_modify: Product = self.product_repository.get_id(id)
        if product_to_modify is None:
            raise ProductNotFoundException

        existing_product :Product= self.product_repository.find_by_code(product.code)
        if existing_product and existing_product.product_id != id:
            raise ProductCodeAlreadyExistsException

        product.product_id = product_to_modify.product_id
        product.status = product_to_modify.status

        self.product_repository.save(product)
        return

    def delete(self,id :int):
        product_to_delete :Product = self.product_repository.get_id(id)
        if product_to_delete is None:
            raise ProductNotFoundException
        product_to_delete.status = Status.INACTIVE
        self.product_repository.save(product_to_delete)
        return


