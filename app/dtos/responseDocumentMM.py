
from marshmallow import Schema, fields

from app.dtos.responseItemDtoMM import ResponseItemDTO
from app.entities.enums.documentType import DocumentType


class ResponseDocumentMM(Schema):

    document_id = fields.Integer(required=True, error_messages={'required': 'The field document_id is required.'})
    client_id = fields.Integer(required=True, error_messages={'required': 'The field client_id is required.'})
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
    document_concept = fields.String(required=True, error_messages={'required': 'The field document_concept is required.'})
    client_type_id = fields.String(required=True, error_messages={'required': 'The field client_type_id is required.'})
    client_tax_id = fields.String(required=True,error_messages={'required': 'The field client_id_number is required.'})
    client_name = fields.String(required=True,error_messages={'required': 'The field client_name is required.'})
    client_tax_condition = fields.String(required=True,error_messages={'required': 'The field client_tax_condition is required.'})
    client_address = fields.String(required=True,error_messages={'required': 'The field client_address is required.'})
    client_city = fields.String(required=True,error_messages={'required': 'The field client_city is required.'})
    client_state = fields.String(required=True,error_messages={'required': 'The field client_state is required.'})

    date = fields.Method(
        required=True,
        serialize="format_date",
        error_messages={'required': 'The field date is required.'}
    )

    date_serv_from = fields.Method(
        required=False,
        serialize="format_date_serv_from",
    )

    date_serv_to = fields.Method(
        required=False,
        serialize="format_date_serv_to",
    )

    expiration_date = fields.Method(
        required=False,
        serialize="format_expiration_date",
    )
    total_amount = fields.Method(
        required=True,
        serialize="format_total_amount",
        error_messages={'required': 'The field total_amount is required.'}
    )
    taxable_amount = fields.Method(
        required=True,
        serialize="format_taxable_amount",
        error_messages={'required': 'The field taxable_amount is required.'}
    )

    exempt_amount = fields.Float(required=True, error_messages={'required': 'The field exempt_amount is required.'})
    no_grav_amount = fields.Float(required=True, error_messages={'required': 'The field no_grav_amount is required.'})
    tributes_amount = fields.Float(required=True, error_messages={'required': 'The field tributes_amount is required.'})
    tax_amount = fields.Method(
        required=True,
        serialize="format_tax_amount",
        error_messages={'required': 'The field tax_amount is required.'}
    )

    currency = fields.String(required=True, error_messages={'required': 'The field currency is required.'})
    exchange_rate = fields.Float(required=True, error_messages={'required': 'The field exchange_rate is required.'})
    cae = fields.Method(
        required=False,
        allow_none=True,
        serialize="format_cae",
    )

    cae_vto = fields.Method(
        required=False,
        allow_none=True,
        serialize = "format_cae_vto",
    )
    items = fields.List(fields.Nested(ResponseItemDTO), required=True, error_messages={'required': 'The field items is required.'})

    def format_number(self, obj):
        return f"{obj.get('number'):08}"

    def format_pos(self, obj):
        return f"{obj.get('pos'):05}"

    def format_date(self, obj):
        expiration_date = obj.get('expiration_date')
        return expiration_date.strftime('%d-%m-%Y') if expiration_date else "N/A"

    def format_date_serv_from(self, obj):
        date_serv_from = obj.get('date_serv_from')
        return date_serv_from.strftime('%d-%m-%Y') if date_serv_from else "N/A"

    def format_date_serv_to(self, obj):
        date_serv_to = obj.get('date_serv_to')
        return date_serv_to.strftime('%d-%m-%Y') if date_serv_to else "N/A"

    def format_expiration_date(self, obj):
        expiration_date = obj.get('expiration_date')
        return expiration_date.strftime('%d-%m-%Y') if expiration_date else "N/A"

    def format_cae_vto(self, obj):
        cae_vto = obj.get('cae_vto')
        return cae_vto.strftime('%d-%m-%Y') if cae_vto else "N/A"

    def format_cae(self, obj):
        cae = obj.get('cae')
        return cae if cae else "N/A"

    def format_date(self, obj):
        date = obj.get('date')
        return date.strftime('%d-%m-%Y')

    def format_taxable_amount(self, obj):
        return f" {float(obj.get('taxable_amount')):,.2f}"

    def format_total_amount(self, obj):
        return f" {float(obj.get('total_amount')):,.2f}"

    def format_tax_amount(self, obj):
        return f" {float(obj.get('tax_amount')):,.2f}"

    def format_document_type(self, obj):
        document_type = obj.get('document_type')

        if isinstance(document_type, str):
            try:
                document_type = DocumentType[document_type]
            except KeyError:
                return {"document": "UNKNOWN", "letter": "?", "value": "?"}

        if not isinstance(document_type, DocumentType):
            return {"document": "UNKNOWN", "letter": "?","value": "?"}

        return {
            "document": document_type.get_document(),
            "letter": document_type.get_letra(),
            "value":document_type.get_value()
        }



