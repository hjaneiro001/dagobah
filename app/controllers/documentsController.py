
from flask import Blueprint, jsonify, request, send_file, logging

import io
import base64

from app.dtos.requestDocument import RequestDocumentDTO
from app.dtos.responseDocumentMM import ResponseDocumentMM
from app.entities.document import Document, DocumentBuilder
from app.entities.enums.currency import Currency
from app.entities.enums.documentType import DocumentType
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
                          .document_type(DocumentType.get_document_type((post_document_dto["document_type"])))
                          .date(post_document_dto["date"])
                          .date_serv_from(post_document_dto["date_serv_from"])
                          .date_serv_to(post_document_dto["date_serv_to"])
                          .expiration_date(post_document_dto["expiration_date"])
                          .build())

    items = []

    for item_data in post_document_dto["items"]:
        item :Item = (
            ItemBuilder()
            .product(item_data["product_id"])
            .quantity(item_data["quantity"])
            .unit_price(item_data["unit_price"])
            .discount((item_data["discount"]))
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

    image_data = base64.b64decode(base64_image.split(",")[1])
    image_io = io.BytesIO(image_data)
    image_io.seek(0)

    return send_file(image_io, mimetype='image/png')

@documentsBp.route("/certificado/", methods=['GET'])
@handle_exceptions
def get_certificado():

   return documentService.get_certificado()

