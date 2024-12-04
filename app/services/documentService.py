
from app.entities.document import Document
from app.entities.enums.status import Status
from app.exceptions.documentAlreadyExistException import DocumentAlreadyExistsException

class DocumentService:

    def __init__(self, document_repository, item_repository):
        self.document_repository = document_repository
        self.item_repository = item_repository

    def create(self, document: Document, items):

        if self.document_repository.get_document(document):
            raise DocumentAlreadyExistsException

        document.status = Status.ACTIVE.get_value()
        document_id = self.document_repository.create(document)

        for item_data in items:
            item_data.document_id = document_id

        self.item_repository.create(items)

        return document_id