from enum import Enum

class TypeId(Enum):
    CUIT = ['CUIT',80]
    CUIL = ['CUIL',86]
    DNI = ['DNI',96]
    CF = ['CF',99]

    def get_type_id(value):
        for item in TypeId:
            if value in item.value:
                return item
        return None

    def get_type(self):
        return self.value[0]

    def get_code(self):
        return self.value[1]

