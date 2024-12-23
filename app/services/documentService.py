from app.dtos.documentAfipDto import DocumentAfipDto
from app.entities.document import Document
from app.entities.enums.status import Status
from app.entities.item import Item
from app.exceptions.documentAlreadyExistException import DocumentAlreadyExistsException
from app.exceptions.documentNotFoundException import DocumentNotFoundException
from app.factories.documentAfipDTOFactory  import DocumentAfipDTOFactory


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

        documentDTO :DocumentAfipDto = DocumentAfipDTOFactory.from_entity(document,items)
        res = self.sdk_afip_repository.create_document_afip(documentDTO)
        
        document_id = self.document_repository.create(document)
        self.item_repository.create(items, document_id)

        return (res)

    def get_all(self):

        document_list = self.document_repository.get_all()

        return(document_list)

    def get_id(self, id :int):

        document_data = self.document_repository.get_id(id)

        if document_data is None:
            raise DocumentNotFoundException

        return(document_data)
