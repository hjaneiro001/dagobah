from datetime import datetime
from typing import List

from app.entities.enums.currency import Currency
from app.entities.enums.documentConcept import DocumentConcept
from app.entities.enums.documentType import DocumentType
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.typeId import TypeId

class Document:
    def  __init__(self, document_id :int, client_id :int, pos :int, document_type :DocumentType, document_concept :DocumentConcept,
                  client_type_id :TypeId, client_tax_id :str,client_tax_condition: TaxCondition, client_name :str, client_address :str, client_city :str, client_state :str, number :int,
                  date :datetime, date_serv_from :datetime, date_serv_to : datetime, expiration_date :datetime,total_amount :float,
                  taxable_amount :float, exempt_amount :float, no_grav_amount: float, tributes_amount :float, tax_amount :float,
                  currency :Currency, exchange_rate :float, cae :str, cae_vto :datetime, items :List = None):

        self.document_id :int = document_id
        self.client_id :int = client_id
        self.pos :int = pos
        self.document_type: DocumentType = document_type
        self.document_concept: DocumentConcept = document_concept
        self.client_type_id: TypeId = client_type_id
        self.client_tax_id: str = client_tax_id
        self.client_name :str = client_name
        self.client_address :str = client_address
        self.client_city :str = client_city
        self.client_state :str = client_state
        self.client_tax_condition: TaxCondition = client_tax_condition
        self.number :int = number
        self.date: datetime = date
        self.date_serv_from = date_serv_from
        self.date_serv_to = date_serv_to
        self.expiration_date :datetime = expiration_date
        self.total_amount :float = total_amount
        self.taxable_amount :float = taxable_amount
        self.exempt_amount :float = exempt_amount
        self.no_grav_amount :float = no_grav_amount
        self.tributes_amount :float = tributes_amount
        self.tax_amount :float = tax_amount
        self.currency :Currency = currency
        self.exchange_rate :float = exchange_rate
        self.cae :str = cae
        self.cae_vto :datetime = cae_vto
        self.items: list = items or []


    def __str__(self):

        return (f"Punto de Venta: {self.pos}\n"
                f"Codigo de Cliente: {self.client_id}\n"
                f"Numero de Documento: {self.number}\n"
                f"Tipo de documento: {self.document_type}\n"
                f"Concepto : {self.document_concept}\n"
                f"Tipo ID Cliente : {self.client_type_id}\n"
                f"Numero de ID Cliente : {self.client_tax_id}\n"
                f"Nombre del Cliente : {self.client_name}\n"
                f"Direccion del Cliente : {self.client_address}\n"
                f"Ciudad del Cliente : {self.client_city}\n"
                f"Estado del Cliente : {self.client_state}\n"
                f"Condicion Fiscal : {self.client_tax_condition}\n"
                f"Fecha : {self.date}\n"
                f"Fecha Servicio desde : {self.date_serv_from}\n"
                f"Fecha Servicio hasta : {self.date_serv_to}\n"
                f"Fecha de vencimiento : {self.expiration_date}\n"
                f"Total de la factura : {self.total_amount}\n"
                f"Importe antes de Iva : {self.taxable_amount}\n"
                f"Importe Exento : {self.exempt_amount}\n"
                f"Importe No Gravado : {self.no_grav_amount}\n"
                f"Importe Total de Tributos : {self.tributes_amount}\n"
                f"Importe Exento : {self.exempt_amount}\n"
                f"Importe Iva : {self.tax_amount}\n"
                f"Moneda : {self.currency}\n"
                f"Cotizacion: {self.exchange_rate}\n"
                f"Cae: {self.cae}\n"
                f"Venc. CAE : {self.cae_vto}\n"
                f"Items : {self.items}\n"
                )

    def to_dict(self):

        return {
            "document_id": self.document_id,
            "client_id": self.client_id,
            "pos": self.pos,
            # "document_type": self.document_type.get_type(),
            "document_type": self.document_type,
            "document_concept": self.document_concept.get_concept(),
            "client_type_id": self.client_type_id.get_type(),
            "client_tax_id" : self.client_tax_id,
            "client_name" : self.client_name,
            "client_address" : self.client_address,
            "client_city": self.client_city,
            "client_state": self.client_state,
            "client_tax_condition": self.client_tax_condition,
            "number": self.number,
            "date": self.date if self.date else None,
            "date_serv_from": self.date_serv_from if self.date_serv_from else None,
            "dtae_serv_to": self.date_serv_to if self.date_serv_to else None,
            "expiration_date": self.expiration_date if self.expiration_date else None,
            "total_amount": self.total_amount,
            "taxable_amount": self.taxable_amount,
            "exempt_amount": self.exempt_amount,
            "no_grav_amount": self.no_grav_amount,
            "tributes_amount": self.tributes_amount,
            "tax_amount": self.tax_amount,
            "currency": self.currency.get_value(),
            "exchange_rate": self.exchange_rate,
            "cae": self.cae,
            "Vencimiento CAE": self.cae_vto if self.cae_vto else None,
            "items": [item.to_dict() for item in self.items] if self.items else [],
        }

    def __eq__(self, other):
        if isinstance(other, Document):
            return (self.document_id == other.document_id and
                    self.client_id == other.client_id and
                    self.pos == other.pos and
                    self.document_type == other.document_type and
                    self.document_concept == other.document_concept and
                    self.client_type_id == other.client_type_id and
                    self.client_tax_id == other.client_tax_id and
                    self.client_name == other.client_name and
                    self.client_address == other.client_address and
                    self.client_city == other.client_city and
                    self.client_state == other.client_state and
                    self.client_tax_condition == other.client_tax_condition and
                    self.number == other.number and
                    self.date == other.date and
                    self.date_serv_from == other.date_serv_to and
                    self.date_serv_from == other.date_serv_from and
                    self.expiration_date == other.expiration_date and
                    self.total_amount == other.total_amount and
                    self.taxable_amount == other.taxable_amount and
                    self.exempt_amount == other.exempt_amount and
                    self.no_grav_amount == other.no_grav_amount and
                    self.tributes_amount == other.tributes_amount and
                    self.tax_amount == other.tax_amount and
                    self.currency == other.currency and
                    self.exchange_rate == other.exchange_rate and
                    self.cae == other.cae and
                    self.cae_vto == other.cae_vto and
                    self.items == other.items
                    )

        return False

class DocumentBuilder:
    def __init__(self):
        self._document_id = None
        self._client_id = None
        self._pos = None
        self._document_type = None
        self._document_concept = None
        self._client_type_id = None
        self._client_tax_id = None
        self._client_name = None
        self._client_address = None
        self._client_city = None
        self._client_state = None
        self._client_tax_condition = None
        self._number = None
        self._date = None
        self._date_serv_from = None
        self._date_serv_to = None
        self._expiration_date = None
        self._total_amount = None
        self._taxable_amount = None
        self._exempt_amount = None
        self._no_grav_amount = None
        self._tributes_amount = None
        self._tax_amount = None
        self._currency = None
        self._exchange_rate = None
        self._cae = None
        self._cae_vto = None
        self._items = []


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

    def client_type_id(self, client_type_id: TypeId):
        self._client_type_id: TypeId = client_type_id
        return self

    def client_tax_id(self, client_tax_id: str):
        self._client_tax_id: str = client_tax_id
        return self

    def client_name(self, client_name: str):
        self._client_name: str = client_name
        return self

    def client_address(self, client_address: str):
        self._client_address: str = client_address
        return self

    def client_city(self, client_city: str):
        self._client_city: str = client_city
        return self

    def client_state(self, client_state: str):
        self._client_state: str = client_state
        return self

    def client_tax_condition(self, client_tax_condition: str):
        self._client_tax_condition: str = client_tax_condition
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
        self._date_serv_to: datetime = date_serv_to
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

    def no_grav_amount(self, no_grav_amount):
        self._no_grav_amount: float = no_grav_amount
        return self

    def tributes_amount(self, tributes_amount):
        self._tributes_amount: float = tributes_amount
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

    def cae(self,cae):
        self._cae :str = cae
        return self

    def cae_vto(self,cae_vto):
        self._cae_vto :datetime= cae_vto
        return self

    def items(self, items: list):
        self._items = items
        return self

    def build(self):
        return Document(
            document_id=self._document_id,
            client_id=self._client_id,
            pos=self._pos,
            document_type=self._document_type,
            document_concept=self._document_concept,
            client_type_id=self._client_type_id,
            client_tax_id=self._client_tax_id,
            client_name=self._client_name,
            client_address=self._client_address,
            client_city=self._client_city,
            client_state=self._client_state,
            client_tax_condition=self._client_tax_condition,
            number=self._number,
            date=self._date,
            date_serv_from=self._date_serv_from,
            date_serv_to=self._date_serv_to,
            expiration_date=self._expiration_date,
            total_amount=self._total_amount,
            taxable_amount=self._taxable_amount,
            exempt_amount=self._exempt_amount,
            no_grav_amount=self._no_grav_amount,
            tributes_amount=self._tributes_amount,
            tax_amount=self._tax_amount,
            currency=self._currency,
            exchange_rate=self._exchange_rate,
            cae=self._cae,
            cae_vto=self._cae_vto,
            items = self._items
        )


