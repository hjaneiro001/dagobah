from app.entities.document import Document
from app.entities.enums.status import Status
from app.exceptions.documentAlreadyExistException import DocumentAlreadyExistsException


class DocumentService:
    def __init__(self, document_repository):
        self.document_repository = document_repository

    def create(self,document: Document):

         if self.document_repository.get_document(document):
             raise DocumentAlreadyExistsException
         document.status = Status.ACTIVE
         document_id = self.document_repository.create(document)
         return document_id
