from marshmallow import Schema, fields

from app.entities.enums.documentType import DocumentType


class ResponseDocumentIssued(Schema):
    document_id = fields.Integer(required=True, error_messages={'required': 'The field document_id is required.'})
    pos = fields.Method(
        required=True,
        serialize="format_pos",
        error_messages={'required': 'The field pos is required.'}
    )
    number = fields.Method(
        required=True,
        serialize="format_number",
        error_messages={'required': 'The field number is required.'}
    )
    document_type = fields.Method(
        required=True,
        serialize="format_document_type",
        error_messages={'required': 'The field document_type is required.'}
    )

    def format_number(self, obj):
        return f"{obj.get('number'):08}"

    def format_pos(self, obj):
        return f"{obj.get('pos'):05}"

    def format_document_type(self, obj):
        document_type_str = obj.get("document_type")  # Aquí llega como string
        document_type_enum = DocumentType.get_document_type(document_type_str)  # Convertimos a Enum
        return document_type_enum.get_letra() if document_type_enum else None

