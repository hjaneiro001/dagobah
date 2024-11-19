from itertools import product

from app.entities.product import Product

class Item:
    def __init__(self,item_id :int, product :Product, quantity: float, tax_rate :float, unit_price :float):

        self.item_id :int = item_id
        self.product :Product = product
        self.quantity :float = quantity
        self.tax_rate :float = tax_rate
        self.unit_price :float = unit_price

    def __str__(self):

        return (f"Producto: {self.product}\n"
                f"Cantidad: {self.quantity}\n"
                f"Iva: {self.tax_rate}\n"
                f"Precio uniario: {self.unit_price}\n"
                )

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "product": self.product,
            "quantity": self.quantity,
            "tax_rate": self.tax_rate,
            "unit_price": self.unit_price
        }

    def __eq__(self, other):
        if isinstance(other, Item):
            return {self.item_id == other.item_id and
                    self.product == other.product and
                    self.quantity == other.quantity and
                    self.tax_rate == other.tax_rate and
                    self.unit_price == other.unit_price
        }

        return False

    class ItemBuilder:
        def __init__(self):
            self._item_id = None
            self._product = None
            self._quantity = None
            self.tax_rate = None
            self._unit_price = None

        def item_id(self,item_id):
            self._item_id :int = item_id
            return self

        def product(self,product):
            self._product :Product = product
            return self

        def quantity(self, quantity):
            self._quantity :float = quantity
            return self

        def tax_rate(self,tax_rate):
            self._tax_rate :float = tax_rate
            return self

        def unit_price(self,unit_price):
            self._unit_price :float = unit_price
            return self

        def build(self):
            return Item(
                item_id=self._item_id,
                product = self._product,
                quantity = self._quantity,
                tax_rate = self._tax_rate,
                unit_price = self._unit_price
            )

