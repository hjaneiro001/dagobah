from marshmallow import Schema, fields

class RequestProductDTO(Schema):
    code = fields.String(required=True, error_messages={'required': 'The field code is required.'})
    name = fields.String(required=True, error_messages={'required': 'The field name is required.'})
    description = fields.String(required=True, error_messages={'required': 'The field description is required.'})
    price = fields.Float(required=True, error_messages={'required': 'The field price is required.'})
    currency = fields.String(required=True, error_messages={'required': 'The field currency is required.'})
    iva = fields.String(required=True, error_messages={'required': 'The field IVA is required.'})
    product_type = fields.String(required=True, error_messages={'required': 'The field product type is required.'})
