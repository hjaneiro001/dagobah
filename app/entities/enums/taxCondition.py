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

    def get_tax_condition(value):
        for item in TaxCondition:
            if value in item.value:
                return item
        return None

    def get_condition(self):
        return self.value[0]
