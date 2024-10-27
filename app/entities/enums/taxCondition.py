from enum import Enum

class TaxCondition(Enum):
    RI = ['RESPONSABLE INSCRIPTO']
    NI = ['RESPONSABLE NO INSCRIPTO']
    NR = ['NO RESPONSABLE']
    EX = ['EXENTO']
    CF = ['CONSUMIDOR FINAL']
    MT = ['MONOTRIBUTO']
    NC = ['NO CATEGORIZADO']
    PE = ['PROVEEDOR EXTERIOR']
    CE = ['CLIENTE EXTERIOR']
    IL = ['IVA LIBERADO']
    AP = ['AGENTE PERCEPCION']
    EV = ['CONTRIBUYENTE EVENTUAL']
    MS = ['MONOTRIBUTO SOCIAL']
    ES = ['EVENTUAL SOCIAL']

    @classmethod
    def get_code(cls, value):
        for item in cls:
            if value == item.value[0]:
                return item.name

    def get_condition(self):
        return self.value[0]
