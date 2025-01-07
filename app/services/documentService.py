from marshmallow import ValidationError

from app.dtos.documentAfipDto import DocumentAfipDto
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.dtos.responseItemDtoMM import ResponseItemDTO
from app.entities.document import Document
from app.entities.enums.status import Status
from app.entities.item import Item
from app.exceptions.documentAlreadyExistException import DocumentAlreadyExistsException
from app.exceptions.documentNotFoundException import DocumentNotFoundException
from app.factories.documentAfipDTOFactory  import DocumentAfipDTOFactory
from app.factories.documentDTOFactory import ResponseDocumentDtoFactory

class DocumentService:

    def __init__(self, document_repository, item_repository, sdk_afip_repository):
        self.document_repository = document_repository
        self.item_repository = item_repository
        self.sdk_afip_repository = sdk_afip_repository

    def create(self, document: Document, items :list[Item]):

        number = self.sdk_afip_repository.next_number(document, items)
        document.number = number
        document.status = Status.ACTIVE.get_value()

        if self.document_repository.get_document(document):
            raise DocumentAlreadyExistsException

        document_id = self.document_repository.create(document)

        if document_id:
            self.item_repository.create(items, document_id)
            documentDTO :DocumentAfipDto = DocumentAfipDTOFactory.from_entity(document,items)
            res = self.sdk_afip_repository.create_document_afip(documentDTO)

            document.cae = res["CAE"]
            document.cae_vto = res["CAEFchVto"]

            self.document_repository.save(document)

        return res

    def get_all(self):

        document_list = self.document_repository.get_all()

        return(document_list)


    def get_id(self, id: int):

        document = self.document_repository.get_id(id)
        if document is None:
            raise DocumentNotFoundException

        items = self.item_repository.get_by_document_id(id)
        document.items = items

        return document


    def get_pdf(self, id: int, mode :str):

        document = self.document_repository.get_id(id)

        if document is None:
            raise DocumentNotFoundException

        items = self.item_repository.get_by_document_id(id)
        document.items = items

        response_schema = ResponseDocumentMM()
        document_data = response_schema.dump(document.to_dict())

        response = self.sdk_afip_repository.create_pdf(document_data, mode)

        return response
