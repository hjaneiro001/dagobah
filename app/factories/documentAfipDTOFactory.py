from collections import defaultdict
from typing import List
from app.dtos.documentAfipDto import DocumentAfipDto
from app.dtos.ivaListAfipDto import TaxItemDto
from app.entities.document import Document
from app.entities.item import Item

class DocumentAfipDTOFactory:
    @staticmethod
    def from_entity(document: Document, items: List[Item]) -> DocumentAfipDto:

        builder = DocumentAfipDto.builder()

        # iva_list = [
        #     {
        #         "Id": item.tax_rate.get_code(),
        #         "BaseImp": item.quantity * item.unit_price,
        #         "Importe": item.quantity * item.unit_price * (item.tax_rate.get_value() / 100)
        #     }
        #     for item in items
        # ]

        grouped_iva = defaultdict(lambda: {"BaseImp": 0, "Importe": 0})

        for item in items:
            id_ = item.tax_rate.get_code()
            base_imp = item.quantity * item.unit_price
            importe = base_imp * (item.tax_rate.get_value() / 100)

            grouped_iva[id_]["BaseImp"] += base_imp
            grouped_iva[id_]["Importe"] += importe

        iva_list = [{"Id": id_, "BaseImp": values["BaseImp"], "Importe": values["Importe"]}
                    for id_, values in grouped_iva.items()]

        print(iva_list)

        document_dto = (builder
                        .cant_reg(1)
                        .pos(document.pos)
                        .document_type(document.document_type.get_value())
                        .concept(document.document_concept.get_value())
                        .client_type_id((document.client_type_id.get_code()))
                        .id_number(document.client_id_number)
                        .document_from(document.number)
                        .document_to(document.number)
                        .document_date(document.date)
                        .total_amount(document.total_amount)
                        .no_grav_amount(document.no_grav_amount)
                        .taxable_amount(document.taxable_amount)
                        .exempt_amount(document.exempt_amount)
                        .tax_amount(document.tax_amount)
                        .tributes_amount(document.tributes_amount)
                        .currency(document.currency.get_id())
                        .exchange_rate(document.exchange_rate)
                        .iva_list(iva_list)
                        .build())

        return document_dto
