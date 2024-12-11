from typing import List

from app.entities.document import Document
from app.entities.item import Item


class DocumentDTOFactory:
    @staticmethod
    def from_entity(document: Document, items :List[Item]):

        iva_list = [
            {
                "Id": item.tax_rate.get_code(),
                "BaseImp": item.quantity * item.unit_price,
                "Importe": item.quantity * item.unit_price * (item.tax_rate.get_value() / 100)
            }
            for item in items
        ]

        return {
            "CantReg": 1,
            "PtoVta": document.pos,
            "CbteTipo": document.document_type.get_value(),
            "Concepto": document.document_concept.get_value(),
            "DocTipo": document.client_type_id.get_code(),
            "DocNro": document.client_id_number,
            "CbteDesde": document.number,
            "CbteHasta": document.number,
            "CbteFch": document.date,
            "ImpTotal": document.total_amount,
            "ImpTotConc": document.exempt_amount,
            "ImpNeto": document.taxable_amount,
            "ImpOpEx": document.exempt_amount,
            "ImpIVA": document.tax_amount,
            "ImpTrib": document.tributes_amount,
            "MonId": document.currency.get_id(),
            "MonCotiz": document.exchange_rate,
            "Iva" : iva_list
        }
