
from marshmallow import fields, Schema

class RequestCompanyDto(Schema):

    company_name = fields.String(required=True, error_messages={'required': 'The field company_name is required.'})
    company_address = fields.String(required=True, error_messages={'required' : 'The field company_address is required.'})
    company_city = fields.String(required=True, error_messages={'required' : 'The field company_city is required.'})
    company_state = fields.String(required=True, error_messages={'required' : 'The field company_state is required.'})
    company_country = fields.String(required=True, error_messages={'required' : 'The field company_country is required.'})
    company_email = fields.String(required=True, error_messages={'required' : 'The field company_email required.'})
    company_phone = fields.String(required=True, error_messages={'required' : 'The field company_phone is required.'})
    company_tax_id = fields.String(required=True, error_messages={'required' : 'The field company_tax_id is required.'})
    company_type_id = fields.String(required=True, error_messages={'required' : 'The field company_type_id is required.'})
    company_tax_condition = fields.String(required=True, error_messages={'required': 'The field company_tax_condition is required.'})


