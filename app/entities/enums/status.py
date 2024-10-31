from enum import Enum

class Status(Enum):

    ACTIVE = ['ACTIVE']
    INACTIVE = ['INACTIVE']

    # def get_status(cls, name):
    #     status_member = cls.__members__.get(name)
    #     if status_member:
    #         return status_member.value[0]
    #     return None
    #
    # def __str__(self):
    #     return self.value[0]


    def get_status(value):
        for item in Status:
            if value in item.value:
                return item
        return None

    def get_value(self):
        return self.value[0]
