from enum import Enum

class TaxCondition(Enum):
    RI = ['RESPONSABLE INSCRIPTO',1]
    NI = ['RESPONSABLE NO INSCRIPTO']
    NR = ['NO RESPONSABLE',15]
    EX = ['EXENTO',4]
    CF = ['CONSUMIDOR FINAL',5]
    MT = ['MONOTRIBUTO',6]
    NC = ['NO CATEGORIZADO',15]
    PE = ['PROVEEDOR EXTERIOR',8]
    CE = ['CLIENTE EXTERIOR',9]
    IL = ['IVA LIBERADO',10]
    AP = ['AGENTE PERCEPCION']
    EV = ['CONTRIBUYENTE EVENTUAL']
    MS = ['MONOTRIBUTO SOCIAL', 13]
    ES = ['EVENTUAL SOCIAL', 16]

    def get_tax_condition(value):
        for item in TaxCondition:
            if value in item.value:
                return item
        return None

    def get_condition(self):
        return self.value[0]

    def get_value(self):
        return self.value[1]


