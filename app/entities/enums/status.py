from enum import Enum

class Status(Enum):

    ACTIVE = ['ACTIVE']
    INACTIVE = ['INACTIVE']

    def get_status(value):
        for item in Status:
            if value in item.value:
                return item
        return None

    def get_value(self):
        return self.value[0]
