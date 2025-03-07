from marshmallow import Schema, fields

class RequestItemDTO(Schema):
    product_id = fields.Integer(required=True, error_messages={'required': 'The field product_id is required.'})
    quantity = fields.Float(required=True, error_messages={'required': 'The field quantity is required.'})
    unit_price = fields.Float(required=True, error_messages={'required': 'The field unit_price is required.'})
    discount = fields.Float(required=True, error_messages={'required': 'The field discount is required.'})
