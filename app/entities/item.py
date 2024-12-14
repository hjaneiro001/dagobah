from app.entities.enums.productIva import ProductIva

class Item:
    def __init__(self,item_id :int,document_id :int, product_id :int, quantity: float, tax_rate :ProductIva, unit_price :float):

        self.item_id :int = item_id
        self.document_id :int = document_id
        self.product_id :int = product_id
        self.quantity :float = quantity
        self.tax_rate :ProductIva = tax_rate
        self.unit_price :float = unit_price

    def __str__(self):

        return (f"Producto: {self.product_id}\n"
                f"Documento: {self.document_id}\n"
                f"Cantidad: {self.quantity}\n"
                f"Iva: {self.tax_rate}\n"
                f"Precio uniario: {self.unit_price}\n"
                )

    def __repr__(self):
        return (f"Item(product_id={self.product_id}, document_id={self.document_id}, "
                f"quantity={self.quantity}, tax_rate={self.tax_rate}, "
                f"unit_price={self.unit_price})")

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "document_id": self.document_id,
            "product": self.product_id,
            "quantity": self.quantity,
            "tax_rate": self.tax_rate,
            "unit_price": self.unit_price
        }

    def __eq__(self, other):
        if isinstance(other, Item):
            return {self.item_id == other.item_id and
                    self.document_id == other.document_id and
                    self.product_id == other.product_id and
                    self.quantity == other.quantity and
                    self.tax_rate == other.tax_rate and
                    self.unit_price == other.unit_price
        }

        return False

class ItemBuilder:
        def __init__(self):
            self._item_id = None
            self._document_id = None
            self._product_id = None
            self._quantity = None
            self._tax_rate = None
            self._unit_price = None

        def item_id(self,item_id):
            self._item_id :int = item_id
            return self

        def document(self,document_id):
            self._document_id :int = document_id
            return self

        def product(self,product_id):
            self._product_id :int = product_id
            return self

        def quantity(self, quantity):
            self._quantity :float = quantity
            return self

        def tax_rate(self,tax_rate):
            self._tax_rate :ProductIva = tax_rate
            return self

        def unit_price(self,unit_price):
            self._unit_price :float = unit_price
            return self

        def build(self):
            return Item(
                item_id=self._item_id,
                document_id=self._document_id,
                product_id = self._product_id,
                quantity = self._quantity,
                tax_rate = self._tax_rate,
                unit_price = self._unit_price
            )

