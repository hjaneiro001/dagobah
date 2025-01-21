from marshmallow import Schema, fields

from app.dtos.requestItemDto import RequestItemDTO

class RequestDocumentDTO(Schema):
    client_id = fields.Integer(required=True, error_messages={'required': 'The field client_id is required.'})
    pos = fields.Integer(required=True, error_messages={'required': 'The field pos is required.'})
    # document_type = fields.String(required=True, error_messages={'required': 'The field document_type is required.'})
    document_concept = fields.String(required=True, error_messages={'required': 'The field document_concept is required.'})
    date = fields.String(required=True, error_messages={'required': 'The field date is required.'})
    expiration_date = fields.String(required=False, allow_none=True)
    total_amount = fields.Float(required=True, error_messages={'required': 'The field total_amount is required.'})
    taxable_amount = fields.Float(required=True, error_messages={'required': 'The field taxable_amount is required.'})
    exempt_amount = fields.Float(required=True, error_messages={'required': 'The field exempt_amount is required.'})
    no_grav_amount = fields.Float(required=True, error_messages={'required': 'The field no_grav_amount is required.'})
    tributes_amount = fields.Float(required=True, error_messages={'required': 'The field tributes_amount is required.'})
    tax_amount = fields.Float(required=True, error_messages={'required': 'The field tax_amount is required.'})
    currency = fields.String(required=True, error_messages={'required': 'The field currency is required.'})
    exchange_rate = fields.Float(required=True, error_messages={'required': 'The field exchange_rate is required.'})
    cae = fields.String(required=False, allow_none=True)
    items = fields.List(fields.Nested(RequestItemDTO), required=True, error_messages={'required': 'The field items is required.'})
