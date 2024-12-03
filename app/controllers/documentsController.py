
from flask import Blueprint, jsonify, request

from app.dtos.requestDocument import RequestDocumentDTO
from app.entities.document import Document, DocumentBuilder
from app.entities.enums.documentConcept import DocumentConcept
from app.entities.enums.documentType import DocumentType
from app.exceptions.wrapperExceptions import handle_exceptions
from app.modules import documentService

documentsBp = Blueprint('documents', __name__)

@documentsBp.route("/", methods=['POST'])
@handle_exceptions
def create():

    post_document_dto = RequestDocumentDTO().load(request.json)


    document :Document = (DocumentBuilder()
                          .client_id(post_document_dto["client_id"])
                          .pos(post_document_dto["pos"])
                          .document_type(DocumentType.get_document_type(post_document_dto["document_type"]))
                          .document_concept(DocumentConcept.get_document_concept(post_document_dto["document_concept"]))
                          .number(post_document_dto["number"])
                          .date(post_document_dto["date"])
                          .date_serv_from(post_document_dto["date_serv_from"])
                          .date_serv_to(post_document_dto["date_serv_to"])
                          .expiration_date(post_document_dto["expiration_date"])
                          .total_amount((post_document_dto["total_amount"]))
                          .taxable_amount(post_document_dto["taxable_amount"])
                          .exempt_amount(post_document_dto["exempt_amount"])
                          .tax_amount(post_document_dto["tax_amount"])
                          .currency(post_document_dto["currency"])
                          .exchange_rate(post_document_dto["exchange_rate"])
                          .build())



    document_id :int  = documentService.create(document)

    return jsonify({"Document id": document_id}), 201
