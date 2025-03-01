from enum import Enum

class Currency(Enum):
    ARS = ['PESOS',"$","PES"]
    USD = ['DOLARES', "U$S", "DOL"]

    def get_currency(value):
        for item in Currency:
            if value in item.value:
                return item
        return None

    def get_value(self):
        return self.value[0]

    def get_denomination(self):
        return self.value[1]

    def get_id(self):
        return self.value[2]

