from marshmallow import Schema, fields

from app.entities.enums.currency import Currency

class ResponseProductDTO(Schema):
    product_id = fields.Integer(required=True, error_messages={'required': 'The field product ID is required.'})
    code = fields.String(required=True, error_messages={'required': 'The field code is required.'})
    bar_code = fields.String(required=True, error_messages={'required': 'The field bar code is required.'})
    name = fields.String(required=True, error_messages={'required': 'The field name is required.'})
    description = fields.String(required=True, error_messages={'required': 'The field description is required.'})
    pack = fields.Float(required=True, error_messages={'required': 'The field pack is required.'})
    price = fields.Method(
        required=True,
        serialize="format_price",
        error_messages={'required': 'The field price is required.'})
    # currency = fields.String(required=True, error_messages={'required': 'The field currency is required.'})
    currency = fields.Method(
        required=True,
        serialize="currency_enum",
        error_messages={'required': 'The field currency is required.'})

    iva = fields.String(required=True, error_messages={'required': 'The field IVA is required.'})
    product_type = fields.String(required=True, error_messages={'required': 'The field product type is required.'})
    status = fields.String(required=True, error_messages={'required': 'The field status is required.'})

    def format_price(self, obj):
        return f"{float(obj.get('price')):,.2f}"

    # def currency_enum(self,obj):
    #     currency_str :str = obj.get('currency')
    #     currency_enum = Currency.get_currency(currency_str)
    #     return currency_enum.get_denomination()


    def currency_enum(self, obj):
        currency_str: str = obj.get('currency')
        currency_enum = Currency.get_currency(currency_str)

        if currency_enum:
           return {
            "denomination": currency_enum.get_denomination(),
            "value": currency_enum.get_value()
        }

        return None
