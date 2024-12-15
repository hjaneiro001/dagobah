from afip import Afip

from app.dtos.documentAfipDto import DocumentAfipDto
from app.entities.document import Document
from app.entities.item import Item

class SdkAfipRepository:

    def __init__(self):
        self.afip = Afip({"CUIT": 20409378472})

    def next_number(self,document :Document, items :list[Item]):

        document_number = self.afip.ElectronicBilling.getLastVoucher(document.pos,document.document_type.get_value())
        next_number = document_number + 1

        return next_number

    def create_document_afip(self,documentDTO :DocumentAfipDto):

        return_full_response = False
        # documentDTO = {
        #     "CantReg": 1,  # Cantidad de comprobantes a registrar
        #     "PtoVta": 2,  # Punto de venta
        #     "CbteTipo": 1,  # Tipo de comprobante (ver tipos disponibles)
        #     "Concepto": 1,  # Concepto del Comprobante: (1)Productos, (2)Servicios, (3)Productos y Servicios
        #     "DocTipo": 80,  # Tipo de documento del comprador (99 consumidor final, ver tipos disponibles)
        #     "DocNro": "30710914911",  # Número de documento del comprador (0 consumidor final)
        #     "CbteDesde": 261,  # Número de comprobante o numero del primer comprobante en caso de ser mas de uno
        #     "CbteHasta": 261,  # Número de comprobante o numero del último comprobante en caso de ser mas de uno
        #     "CbteFch": "20241214",  # (Opcional) Fecha del comprobante (yyyymmdd) o fecha actual si es nulo
        #     "ImpTotal": 121,  # Importe total del comprobante
        #     "ImpTotConc": 0,  # Importe neto no gravado
        #     "ImpNeto": 100,  # Importe neto gravado
        #     "ImpOpEx": 0,  # Importe exento de IVA
        #     "ImpIVA": 21,  # Importe total de IVA
        #     "ImpTrib": 0,  # Importe total de tributos
        #     "MonId": "PES",
        #     # Tipo de moneda usada en el comprobante (ver tipos disponibles)("PES" para pesos argentinos)
        #     "MonCotiz": 1,  # Cotización de la moneda usada (1 para pesos argentinos)
        #     "Iva": [  # (Opcional) Alícuotas asociadas al comprobante
        #         {
        #             "Id": 5,  # Id del tipo de IVA (5 para 21%)(ver tipos disponibles)
        #             "BaseImp": 100,  # Base imponible
        #             "Importe": 21  # Importe
        #         }
        #     ]
        # }

        res = self.afip.ElectronicBilling.createVoucher(documentDTO.to_dict(), return_full_response)

        res["CAE"]
        res["CAEFchVto"]

        print(res)

        return(res)