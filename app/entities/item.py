class Item:
    def __init__(self,item_id :int, product_id :int, quantity: float, unit_price :float, discount :float, product_name :str, product_code :str):

        self.item_id :int = item_id
        self.product_id :int = product_id
        self.quantity :float = quantity
        self.unit_price :float = unit_price
        self.discount :float = discount
        self.product_name :str = product_name
        self.product_code :str = product_code

    def __str__(self):

        return (f"Producto: {self.product_id}\n"
                f"Cantidad: {self.quantity}\n"
                f"Precio uniario: {self.unit_price}\n"
                f"Discount : {self.discount}\n "
                f"Nombre producto : {self.product_name}\n"
                f"Codigo producto : {self.product_code}\n"
                )

    def __repr__(self):
        return (f"Item(product_id={self.product_id},"
                f"quantity={self.quantity},"
                f"unit_price={self.unit_price}),"
                f"discount={self.discount}")

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "product": self.product_id,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "discount": self.discount,
            "product_name": self.product_name,
            "product_code": self.product_code
        }

    def __eq__(self, other):
        if isinstance(other, Item):
            return {self.item_id == other.item_id and
                    self.product_id == other.product_id and
                    self.quantity == other.quantity and
                    self.unit_price == other.unit_price and
                    self.discount == other.discount and
                    self.product_name == other.product_name and
                    self.product_code == other.product_code
        }

        return False

class ItemBuilder:
        def __init__(self):
            self._item_id = None
            self._product_id = None
            self._quantity = None
            self._unit_price = None
            self._discount = None
            self._product_name = None
            self._product_code = None

        def item_id(self,item_id):
            self._item_id :int = item_id
            return self

        def product(self,product_id):
            self._product_id :int = product_id
            return self

        def quantity(self, quantity):
            self._quantity :float = quantity
            return self

        def unit_price(self,unit_price):
            self._unit_price :float = unit_price
            return self

        def discount(self,discount):
            self._discount :float = discount
            return self

        def product_name(self,product_name):
            self._product_name :str = product_name
            return self

        def product_code(self,product_code):
            self._product_code = product_code
            return self

        def build(self):
            return Item(
                item_id=self._item_id,
                product_id = self._product_id,
                quantity = self._quantity,
                unit_price = self._unit_price,
                discount = self._discount,
                product_name = self._product_name,
                product_code =self._product_code
            )

