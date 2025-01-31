from marshmallow import Schema, fields

from app.dtos.requestItemDto import RequestItemDTO

class RequestDocumentDTO(Schema):
    client_id = fields.Integer(required=True, error_messages={'required': 'The field client_id is required.'})
    document_type = fields.String(required=True, error_messages={'required': 'The field document_type is required.'})
    date = fields.String(required=True, error_messages={'required': 'The field date is required.'})
    date_serv_from = fields.String(required=False, allow_none=True)
    date_serv_to = fields.String(required=False, allow_none=True)
    expiration_date = fields.String(required=False, allow_none=True)
    currency = fields.String(required=True, error_messages={'required': 'The field currency is required.'})
    exchange_rate = fields.Float(required=True, error_messages={'required': 'The field exchange_rate is required.'})
    cae = fields.String(required=False, allow_none=True)
    items = fields.List(fields.Nested(RequestItemDTO), required=True, error_messages={'required': 'The field items is required.'})
