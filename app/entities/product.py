from app.entities.enums.status import Status
from app.entities.enums.currency import Currency
from app.entities.enums.productIva import ProductIva
from app.entities.enums.productType import ProductType

class Product:
    def __init__(self, product_id :int, code :str, bar_code :str, name :str, description :str, pack :float,
                 price :float, currency :Currency, iva: ProductIva, product_type :ProductType, status :Status):
        self.product_id :int = product_id
        self.code :str = code
        self.bar_code :str = bar_code
        self.name :str = name
        self.description:str= description
        self.pack :float = pack
        self.price :float= price
        self.currency :Currency= currency
        self.iva :ProductIva= iva
        self.product_type :ProductType= product_type
        self.status :Status= status

    def __str__(self):
        return (f"Code: {self.code}\n"
                f"Bar Code: {self.bar_code}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Pack: {self.pack}\n"
                f"Price: {self.price}\n"
                f"Currency: {self.currency.value}\n"
                f"Iva: {self.iva.value}\n"
                f"Product Type: {self.product_type.value}\n")

    def to_dict(self):
        return {
                "product_id": self.product_id,
                "code": self.code,
                "bar_code": self.bar_code,
                "name": self.name,
                "description": self.description,
                "pack": self.pack,
                "price": self.price,
                "currency": self.currency.get_value(),
                "iva": self.iva.get_iva(),
                "product_type": self.product_type.get_type(),
                "status": self.status.get_value()
            }

    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.product_id == other.product_id and
                    self.code == other.code and
                    self.bar_code == other.bar_code and
                    self.name == other.name and
                    self.description == other.description and
                    self.pack == other.pack and
                    self.price == other.price and
                    self.currency == other.currency and
                    self.iva == other.iva and
                    self.product_type == other.product_type and
                    self.status == other.status)
        return False

    def __repr__(self):
        return (f"Product(product_id={self.product_id}, "
                f"code='{self.code}', "
                f"bar_code='{self.bar_code}', "
                f"name='{self.name}', "
                f"price='{self.price}', "
                f"currency='{self.currency.value}',"
                f"product_type='{self.product_type.get_type()}', "
                f"iva='{self.iva.get_iva()}', "
                f"status='{self.status.value}')")

class ProductBuilder:
    def __init__(self):
        self._product_id = None
        self._code = None
        self._bar_code = None
        self._name = None
        self._description = None
        self._pack = None
        self._price = None
        self._currency = None
        self._iva = None
        self._product_type = None
        self._status = None

    def product_id(self, product_id):
        self._product_id: int = product_id
        return self

    def code(self, code):
        self._code: str = code
        return self

    def bar_code(self, bar_code):
        self._bar_code: str = bar_code
        return self

    def name(self, name):
        self._name: str = name
        return self

    def description(self, description):
        self._description: str = description
        return self

    def pack(self, pack):
        self._pack: float = pack
        return self

    def price(self, price):
        self._price: float = price
        return self

    def currency(self, currency: Currency):
        self._currency: Currency = currency
        return self

    def iva(self, iva: ProductIva):
        self._iva: ProductIva = iva
        return self

    def product_type(self, product_type: ProductType):
        self._product_type: ProductType = product_type
        return self

    def status(self, status: Status):
        self._status: Status = status
        return self

    def build(self):
        return Product(
            product_id=self._product_id,
            code=self._code,
            bar_code=self._bar_code,
            name=self._name,
            description=self._description,
            pack=self._pack,
            price=self._price,
            currency=self._currency,
            iva=self._iva,
            product_type=self._product_type,
            status=self._status
        )
