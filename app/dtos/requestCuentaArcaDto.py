

from marshmallow import Schema, fields


class RequestCuentaArcaDto(Schema):

    user = fields.String(required=True,error_messages={'required' :'The field User is required'})
    password = fields.String(required=True, error_messages={'required': 'The field Password is required'})
    cert_name = fields.String(required=True,error_messages={'required' : 'The field cert_name is required'})
    company_id = fields.Integer(required=True,error_messages={'required' : 'The field company_id is required'})

