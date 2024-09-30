from marshmallow import Schema, fields

class ResponseClientDto(Schema):
    pk_client = fields.String(required=True, error_messages={'required': 'The field pk_client required.'})
    name = fields.String(required=True, error_messages={'required': 'The field name is required.'})
    address = fields.String(required=True, error_messages={'required': 'The field address is required.'})
    city = fields.String(required=True, error_messages={'required': 'The field city is required.'})
    state = fields.String(required=True, error_messages={'required': 'The field state is required.'})
    country = fields.String(required=True, error_messages={'required': 'The field country is required.'})
    email = fields.Email(required=True, error_messages={'required': 'The field email is required.', 'invalid': 'Invalid email format.'})
    phone = fields.String(required=True, error_messages={'required': 'The field phone is required.'})
    type_id = fields.String(required=True, error_messages={'required': 'The field type ID is required.'})
    tax_id = fields.String(required=True, error_messages={'required': 'The field tax ID is required.'})
    tax_condition = fields.String(required=True, error_messages={'required': 'The field tax condition is required.'})
    status = fields.String(required=True, error_messages={'required': 'The field status is required.'})