from marshmallow import Schema, fields

class RequestDocumentDTO(Schema):
    client_id = fields.Integer(required=True, error_messages={'required': 'The field client_id is required.'})
    pos = fields.Integer(required=True, error_messages={'required': 'The field pos is required.'})
    document_type = fields.String(required=True, error_messages={'required': 'The field document_type is required.'})
    document_concept = fields.String(required=True, error_messages={'required': 'The field document_concept is required.'})
    number = fields.Integer(required=True, error_messages={'required': 'The field number is required.'})
    date = fields.DateTime(required=True, error_messages={'required': 'The field date is required.'})
    date_serv_from = fields.DateTime(required=False)
    date_serv_to = fields.DateTime(required=False)
    expiration_date = fields.DateTime(required=True, error_messages={'required': 'The field expiration_date is required.'})
    total_amount = fields.Float(required=True, error_messages={'required': 'The field total_amount is required.'})
    taxable_amount = fields.Float(required=True, error_messages={'required': 'The field taxable_amount is required.'})
    exempt_amount = fields.Float(required=True, error_messages={'required': 'The field exempt_amount is required.'})
    tax_amount = fields.Float(required=True, error_messages={'required': 'The field tax_amount is required.'})
    currency = fields.String(required=True, error_messages={'required': 'The field currency is required.'})
    exchange_rate = fields.Float(required=True, error_messages={'required': 'The field exchange_rate is required.'})
