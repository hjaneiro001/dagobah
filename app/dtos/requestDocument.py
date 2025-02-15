from marshmallow import Schema, fields, validates_schema, ValidationError
from datetime import datetime

from app.dtos.requestItemDto import RequestItemDTO
from app.exceptions.dateExpirationValidationException import DateExpirationValidationException
from app.exceptions.dateFormatValidationException import DateFormatValidationException
from app.exceptions.dateServToValidationException import DateServToValidationException


class RequestDocumentDTO(Schema):
    client_id = fields.Integer(required=True, error_messages={'required': 'The field client_id is required.'})
    document_type = fields.String(required=True, error_messages={'required': 'The field document_type is required.'})
    date = fields.String(required=True, error_messages={'required': 'The field date is required.'})
    date_serv_from = fields.String(required=False, allow_none=True)
    date_serv_to = fields.String(required=False, allow_none=True)
    expiration_date = fields.String(required=False, allow_none=True)
    cae = fields.String(required=False, allow_none=True)
    items = fields.List(fields.Nested(RequestItemDTO), required=True, error_messages={'required': 'The field items is required.'})

    @validates_schema
    def validate_dates(self, data, **kwargs):
        date_format = "%Y%m%d"

        try:
            date = datetime.strptime(data["date"], date_format)
        except ValueError:
            raise DateFormatValidationException

        for field in ["expiration_date"]:
            if field in data and data[field]:
                try:
                    field_date = datetime.strptime(data[field], date_format)
                    if field_date < date:
                        raise DateExpirationValidationException
                except ValueError:
                         raise DateFormatValidationException

        if "date_serv_from" in data and "date_serv_to" in data and data["date_serv_from"] and data["date_serv_to"]:

            try:
                date_serv_from = datetime.strptime(data["date_serv_from"], date_format)
                date_serv_to = datetime.strptime(data["date_serv_to"], date_format)
                if date_serv_to < date_serv_from:
                    raise DateServToValidationException
            except ValueError:
                raise DateFormatValidationException
