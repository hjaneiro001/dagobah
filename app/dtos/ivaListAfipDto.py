class TaxItemDto:
    def __init__(self, id=None, taxable_amount=None, amount=None):
        self.id = id
        self.taxable_amount = taxable_amount
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, TaxItemDto):
            return False
        return (self.id == other.Id and
                self.taxable_amount == other.taxable_amount and
                self.amount == other.amount)

    def __str__(self):
        return f"TaxItem(Id='{self.id}', BaseImp={self.taxable_amount}, Importe={self.amount})"

    def get_id(self):
        return self.Id

    def get_base_imp(self):
        return self.taxable_amount

    def get_amount(self):
        return self.amount

    def set_id(self, id):
        self.id = id

    def set_base_imp(self, taxable_amount):
        self.taxable_amount= taxable_amount

    def set_amount(self, amount):
        self.amount = amount

    def to_dict(self):
        return {
            "Id": self.id,
            "BaseImp": self.taxable_amount,
            "Importe": self.amount
        }

    @classmethod
    def builder(cls):
         return cls.TaxItemBuilder()

    class TaxItemBuilder:
        def __init__(self):
            self._id = None
            self._taxable_amount = None
            self._amount = None

        def id(self, id_enum):
            self._id = id_enum.get_code() if hasattr(id_enum, 'get_code') else id_enum
            return self

        def imp(self, taxable_amount):
            self._taxable_amount = taxable_amount
            return self

        def importe(self, amount):
            self._amount = amount
            return self

        def build(self):

            return TaxItemDto(
                id=self._id,
                taxable_amount=self._taxable_amount,
                amount=self._amount)
