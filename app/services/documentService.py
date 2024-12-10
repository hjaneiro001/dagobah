
from app.entities.document import Document
from app.entities.enums.status import Status
from app.entities.item import Item

class DocumentService:

    def __init__(self, document_repository, item_repository, sdk_afip_repository):
        self.document_repository = document_repository
        self.item_repository = item_repository
        self.sdk_afip_repository = sdk_afip_repository

    def create(self, document: Document, items :list[Item]):

        number = self.sdk_afip_repository.next_number(document, items)
        document.number = number
        document.status = Status.ACTIVE.get_value()
        #
        # if self.document_repository.get_document(document):
        #     raise DocumentAlreadyExistsException

        # documentDTO = DocumentDTOFactory.from_entity(document,items)
        # print(documentDTO)
        documentDTO = {
                        'CantReg': 1,
                        'PtoVta': 2,
                        'CbteTipo': 1,
                        'Concepto': 1,  # Código para 'BIENES'
                        'DocTipo': 80,  # Código para 'FACTURA' (debería ser el tipo de documento del receptor, como CUIT o DNI)
                        'DocNro': 30710914911,
                        'CbteDesde': number,
                        'CbteHasta': number,
                        'CbteFch': '20241209',
                        'ImpTotal': 1710.0,
                        'ImpTotConc': 500.0,
                        'ImpNeto': 1000.0,
                        'ImpOpEx': 0,
                        'ImpIVA': 210.0,
                        'ImpTrib': 0,
                        'MonId': 'PES',
                        'MonCotiz': 1.0,
                        'Iva': [
                            {'Id': 5, 'BaseImp': 1000.0, 'Importe': 210.0},  # Id=5 para 21%
                        ]
                    }

        res = self.sdk_afip_repository.create_document_afip(documentDTO)
        print(number)
        return(res)
       # document_id = self.document_repository.create(document)
       # self.item_repository.create(items, document_id)
