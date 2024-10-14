
class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository


    def get_all(self):
        return self.product_repository.get_all()




