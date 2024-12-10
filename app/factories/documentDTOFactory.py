from typing import List

from app.entities.document import Document
from app.entities.item import Item


class DocumentDTOFactory:
    @staticmethod
    def from_entity(document: Document, items :List[Item]):

        iva_list = [
            {
                "Id": item.tax_rate.get_code(),  # Obtiene el código del IVA desde el enum tax_rate
                "BaseImp": item.quantity * item.unit_price,  # Base imponible = cantidad * precio unitario
                "Importe": item.quantity * item.unit_price * (item.tax_rate.get_value() / 100)  # Monto del IVA
            }
            for item in items
        ]

        return {
            "CantReg": 1,
            "PtoVta": document.pos,
            "CbteTipo": document.document_type.get_value(),
            "Concepto": document.document_concept.get_value(),
            "DocTipo": document.client_type_id.get_code(),
            "DocNro": 0,
            "CbteDesde": document.number,
            "CbteHasta": document.number,
            "CbteFch": "20241208", #ojo fecha harcodeada
            "ImpTotal": document.total_amount,
            "ImpTotConc": document.exempt_amount,
            "ImpNeto": document.taxable_amount,
            "ImpOpEx": 0,
            "ImpIVA": document.tax_amount,
            "ImpTrib": 0,
            "MonId": document.currency.get_id(),
            "MonCotiz": document.exchange_rate,
            "Iva" : iva_list

            #
            # "Iva": [
            #     {
            #         "Id": 5,  # Ajusta el ID del IVA según la alícuota
            #         "BaseImp": document.taxable_amount,
            #         "Importe": document.tax_amount,
            #     }
            # ]
        }


#"CbteFch": document.date.strftime("%Y%m%d") if document.date else None,