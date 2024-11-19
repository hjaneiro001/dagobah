from datetime import datetime

from app.entities.enums.currency import Currency
from app.entities.enums.documentConcept import DocumentConcept
from app.entities.enums.documentType import DocumentType
from app.entities.enums.status import Status

class Document:
    def  __init__(self, document_id :int, client_id :int, pos :int, document_type :DocumentType, document_concept :DocumentConcept,
                  number :int, date :datetime, date_serv_from :datetime, date_serv_to :datetime,
                  expiration_date :datetime,total_amount :float, taxable_amount :float, exempt_amount :float, tax_amount :float, currency :Currency,
                  exchange_rate :float, status :Status):

        self.document_id :int = document_id
        self.client_id :int = client_id
        self.pos :int = pos
        self.document_type: DocumentType = document_type
        self.document_concept: DocumentConcept = document_concept
        self.number :int = number
        self.date: datetime = date
        self.date_serv_from :datetime = date_serv_from
        self.date_serv_to :datetime = date_serv_to
        self.expiration_date :datetime = expiration_date
        self.total_amount :float = total_amount
        self.taxable_amount :float = taxable_amount
        self.exempt_amount :float = exempt_amount
        self.tax_amount :float = tax_amount
        self.currency :Currency = currency
        self.exchange_rate :float = exchange_rate
        self.status :Status = status

    def __str__(self):

        return (f"Punto de Venta: {self.pos}\n"
                f"Codigo de Cliente: {self.client_id}\n"
                f"Numero de Documento: {self.tax_id}\n"
                f"Tipo de documento: {self.document_type}\n"
                f"Concepto : {self.document_concept}\n"
                f"Fecha : {self.date}\n"
                f"Fecha del servicio desde : {self.date_serv_from}\n"
                f"Fecha del servicio hasta : {self.date_serv_to}\n"
                f"Fecha de vencimiento : {self.expiration_date}\n"
                f"Total de la factura : {self.total_amount}\n"
                f"Importe antes de Iva : {self.taxable_amount}\n"
                f"Importe Exento : {self.exempt_amount}\n"
                f"Importe Iva : {self.tax_amount}\n"
                f"Moneda : {self.currency}\n"
                f"Cotizacion: {self.exchange_rate}\n"
                f"Status : {self.status}\n"
                )

    def to_dict(self):
        return {
            "document_id": self.document_id,
            "client_id": self.client_id,
            "pos": self.pos,
            "document_type": self.document_type.get_type(),
            "document_concept": self.document_concept.get_concept(),
            "number": self.number,
            "date": self.date.isoformat() if self.date else None,
            "date_serv_from": self.date_serv_from.isoformat() if self.date_serv_from else None,
            "date_serv_to": self.date_serv_to.isoformat() if self.date_serv_to else None,
            "expiration_date": self.expiration_date.isoformat() if self.expiration_date else None,
            "total_amount": self.total_amount,
            "taxable_amount": self.taxable_amount,
            "exempt_amount": self.exempt_amount,
            "tax_amount": self.tax_amount,
            "currency": self.currency.get_currency(),
            "exchange_rate": self.exchange_rate,
            "status": self.status.value,
        }

    def __eq__(self, other):
        if isinstance(other, Document):
            return {self.document_id == other.document_id and
             self.client_id == other.client_id and
             self.pos == other.pos and
             self.document_type == other.document_type and
             self.document_concept == other.document_concept and
             self.number == other.number and
             self.date == other.date and
             self.date_serv_from == other.date_serv_from and
             self.date_serv_to == other.date_serv_to and
             self.expiration_date == other.expiration_date and
             self.total_amount == other.total_amount and
             self.taxable_amount == other.taxable_amount and
             self.exempt_amount == other.exempt_amount and
             self.tax_amount == other.tax_amount and
             self.currency == other.currency and
             self.exchange_rate == other.exchange_rate and
        }

        return False

class DocumentBuilder:
    def __init__(self):
        self._document_id = None
        self._client_id = None
        self._pos = None
        self._document_type = None
        self._document_concept = None
        self._number = None
        self._date = None
        self._date_serv_from = None
        self._date_serv_to = None
        self._expiration_date = None
        self._total_amount = None
        self._taxable_amount = None
        self._exempt_amount = None
        self._tax_amount = None
        self._currency = None
        self._exchange_rate = None
        self._status = None


    def document_id(self, document_id):
        self._document_id :int = document_id
        return self


    def client_id(self, client_id):
        self._client_id :int = client_id
        return self

    def pos(self, pos):
        self._pos :int = pos
        return self

    def document_type(self, document_type :DocumentType):
        self._document_type :DocumentType = document_type
        return self

    def document_concept(self, document_concept :DocumentConcept):
        self._document_concept :DocumentConcept = document_concept
        return self

    def number(self, number):
        self._number :int = number
        return self

    def date(self, date):
        self._date :datetime = date
        return self

    def date_serv_from(self, date_serv_from):
        self._date_serv_from :datetime = date_serv_from
        return self

    def date_serv_to(self, date_serv_to):
        self._date_serv_to :datetime = date_serv_to
        return self

    def expiration_date(self, expiration_date):
        self._expiration_date :datetime = expiration_date
        return self

    def total_amount(self, total_amount):
        self._total_amount :float = total_amount
        return self

    def taxable_amount(self, taxable_amount):
        self._taxable_amount :float = taxable_amount
        return self

    def exempt_amount(self, exemp_amount):
        self._exempt_amount :float = exemp_amount
        return self

    def tax_amount(self, tax_amount):
        self._tax_amount :float = tax_amount
        return self

    def currency(self,currency :Currency):
        self._currency :Currency = currency
        return self

    def exchange_rate(self,exchange_rate):
        self._exchange_rate :float = exchange_rate
        return self

    def status(self,status :Status):
        self._status :Status = status
        return self

    def build(self):
        return Document(
            document_id=self._document_id,
            client_id=self._client_id,
            pos=self._pos,
            document_type=self._document_type,
            document_concept=self._document_concept,
            number=self._number,
            date=self._date,
            date_serv_from=self._date_serv_from,
            date_serv_to=self._date_serv_to,
            expiration_date=self._expiration_date,
            total_amount=self._total_amount,
            taxable_amount=self._taxable_amount,
            exempt_amount=self._exempt_amount,
            tax_amount=self._tax_amount,
            currency=self._currency,
            exchange_rate=self._exchange_rate,
            status=self._status
        )


