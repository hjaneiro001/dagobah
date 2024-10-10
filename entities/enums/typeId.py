from enum import Enum

class TypeId(Enum):
    CUIT = 'CUIT'
    DNI = 'DNI'
    CI = 'CEDULA DE IDENTIDAD'
    PP = 'PASAPORTE'
    LC = 'LIBRETA CIVICA'
    LE = 'LIBRETA DE ENROLAMIENTO'
    ET = 'EN TRAMITE'
