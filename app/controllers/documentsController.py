from http.client import responses
import traceback
from flask import Blueprint, jsonify, request, send_file, logging

import io
import base64

from app.dtos.requestDocument import RequestDocumentDTO
from app.dtos.responseDocumentDto import ResponseDocumentDto
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.document import Document, DocumentBuilder
from app.entities.enums.currency import Currency
from app.entities.enums.documentConcept import DocumentConcept
from app.entities.enums.documentType import DocumentType
from app.entities.enums.productIva import ProductIva
from app.entities.enums.typeId import TypeId
from app.entities.item import Item, ItemBuilder
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
                          .client_type_id(TypeId.get_type_id(post_document_dto["client_type_id"]))
                          .client_id_number(post_document_dto["client_id_number"])
                          .date(post_document_dto["date"])
                          .expiration_date(post_document_dto["expiration_date"])
                          .total_amount((post_document_dto["total_amount"]))
                          .taxable_amount(post_document_dto["taxable_amount"])
                          .exempt_amount(post_document_dto["exempt_amount"])
                          .no_grav_amount(post_document_dto["no_grav_amount"])
                          .tributes_amount(post_document_dto["tributes_amount"])
                          .tax_amount(post_document_dto["tax_amount"])
                          .currency(Currency.get_currency(post_document_dto["currency"]))
                          .exchange_rate(post_document_dto["exchange_rate"])
                          .build())

    items = []

    for item_data in post_document_dto["items"]:
        item :Item = (
            ItemBuilder()
            .product(item_data["product_id"])
            .quantity(item_data["quantity"])
            .tax_rate(ProductIva.get_product_iva(item_data["tax_rate"]))
            .unit_price(item_data["unit_price"])
            .build()
        )
        items.append(item)

    document_id :int  = documentService.create(document,items)
    return jsonify({"Document id": document_id}), 201


@documentsBp.route("/", methods=['GET'])
@handle_exceptions
def get_all():

    document_data = documentService.get_all()

    if not document_data:
        return "", 204

    response = [dto.to_dict() for dto in document_data]

    return jsonify(response), 200

@documentsBp.route("/<int:id>", methods=['GET'])
@handle_exceptions
def get_id(id :int):

    document :Document = documentService.get_id(id)
    response_schema = ResponseDocumentMM()
    document_response = response_schema.dump(document.to_dict())
    return jsonify(document_response), 200



@documentsBp.route("/bill/<int:id>", methods=['GET'])
@handle_exceptions
def get_bill(id :int):

    pdf_file = documentService.get_pdf(id, "bill")  # Esto debería devolver los bytes del PDF
    pdf_io = io.BytesIO(pdf_file)
    pdf_io.seek(0)

    return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name=f"document_{id}.pdf")

@documentsBp.route("/ticket/<int:id>", methods=['GET'])
@handle_exceptions
def get_ticket(id :int):

    pdf_file = documentService.get_pdf(id, "ticket")  # Esto debería devolver los bytes del PDF
    pdf_io = io.BytesIO(pdf_file)
    pdf_io.seek(0)

    return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name=f"document_{id}.pdf")


@documentsBp.route("/qr/<int:id>", methods=['GET'])
@handle_exceptions
def get_qr(id: int):

    base64_image = documentService.get_qr(id)

    image_data = base64.b64decode(base64_image.split(",")[1])  # Eliminamos "data:image/png;base64,"
    image_io = io.BytesIO(image_data)
    image_io.seek(0)

    return send_file(image_io, mimetype='image/png')