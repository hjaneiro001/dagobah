
from app.dtos.documentAfipDto import DocumentAfipDto
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.client import Client
from app.entities.company import Company
from app.entities.document import Document
from app.entities.enums.status import Status
from app.entities.enums.typeId import TypeId
from app.entities.item import Item
from app.exceptions.documentAlreadyExistException import DocumentAlreadyExistsException
from app.exceptions.documentNotFoundException import DocumentNotFoundException
from app.factories.documentAfipDTOFactory  import DocumentAfipDTOFactory


class DocumentService:

    def __init__(self, document_repository, item_repository, sdk_afip_repository, company_repository, client_repository):
        self.document_repository = document_repository
        self.item_repository = item_repository
        self.sdk_afip_repository = sdk_afip_repository
        self.company_repository = company_repository
        self.client_repository = client_repository

    def create(self, document: Document, items :list[Item]):

        company_id = 1 # Leo company_id del token
        company :Company = self.company_repository.get_id(company_id)

        client :Client = self.client_repository.get_id(document.client_id)
        document.client_type_id = client.type_id
        document.client_tax_id = client.tax_id

        number = self.sdk_afip_repository.next_number(document, items, company)
        document.number = number
        document.status = Status.ACTIVE.get_value()

        if self.document_repository.get_document(document):
            raise DocumentAlreadyExistsException

        document_id = self.document_repository.create(document)

        if document_id:
            self.item_repository.create(items, document_id)
            documentDTO :DocumentAfipDto = DocumentAfipDTOFactory.from_entity(document,items)
            res = self.sdk_afip_repository.create_document_afip(documentDTO,company)

            document.cae = res["CAE"]
            document.cae_vto = res["CAEFchVto"]

            self.document_repository.save(document)

        return res


    def get_all(self):

        company_id = 1  # Leo company_id del token
        company: Company = self.company_repository.get_id(company_id)
        document_list = self.document_repository.get_all(company)

        return(document_list)


    def get_id(self, id: int):

        document = self.document_repository.get_id(id)
        if document is None:
            raise DocumentNotFoundException

        items = self.item_repository.get_by_document_id(id)
        document.items = items

        return document


    def get_pdf(self, id: int, mode :str):

        company_id = 1  # Leo company_id del token
        company: Company = self.company_repository.get_id(company_id)

        document = self.document_repository.get_id(id)

        if document is None:
            raise DocumentNotFoundException

        items = self.item_repository.get_by_document_id(id)
        document.items = items

        response_schema = ResponseDocumentMM()
        document_data = response_schema.dump(document.to_dict())

        response = self.sdk_afip_repository.create_pdf(document_data,company, mode)

        return response

    def get_qr(self, id: int):

        document = self.document_repository.get_id(id)

        if document is None:
            raise DocumentNotFoundException

        items = self.item_repository.get_by_document_id(id)
        document.items = items

        response_schema = ResponseDocumentMM()
        document_data = response_schema.dump(document.to_dict())

        response = self.sdk_afip_repository.create_qr(document_data)

        return response

    def get_certificado(self):

        return self.sdk_afip_repository.create_certificado()
