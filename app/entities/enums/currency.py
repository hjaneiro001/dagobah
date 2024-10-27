from enum import Enum

class Currency(Enum):
    ARS = ['PESOS']
    USD = ['DOLARES']

    @classmethod
    def get_code(cls, value):
        for item in cls:
            if value == item.value[0]:
                return item.name
   
    def get_currency(self):
        return self.value[0]




