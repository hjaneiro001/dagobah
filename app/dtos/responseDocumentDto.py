from datetime import datetime

class ResponseDocumentDto:

    def __init__(self, document_id: int, client_id: int, pos: int, document_type: str,
                 document_concept: str, number: int, date: datetime,date_serv_from :datetime,date_serv_to :datetime,
                 expiration_date: datetime, total_amount: float, taxable_amount: float, exempt_amount: float,
                 no_grav_amount: float, tributes_amount: float, tax_amount: float,
                 currency: str, exchange_rate: float, status: str, client_name: str, client_address: str,
                 client_city: str, client_state: str, client_country: str, client_type_id: str, client_tax_id: str,
                 client_tax_condition: str, cae :str, cae_vto :datetime):


        if not isinstance(date, datetime):
            raise ValueError("`date` debe ser un objeto datetime")
        if not isinstance(total_amount, (int, float)) or total_amount < 0:
            raise ValueError("`total_amount` debe ser un número positivo")

        self.document_id = document_id
        self.client_id = client_id
        self.pos = pos
        self.document_type = document_type
        self.document_concept = document_concept
        self.number = number
        self.date = date
        self.date_serv_from = date_serv_from
        self.date_serv_to = date_serv_to
        self.expiration_date = expiration_date
        self.total_amount = total_amount
        self.taxable_amount = taxable_amount
        self.exempt_amount = exempt_amount
        self.no_grav_amount = no_grav_amount
        self.tributes_amount = tributes_amount
        self.tax_amount = tax_amount
        self.currency = currency
        self.exchange_rate = exchange_rate
        self.status = status
        self.client_name = client_name
        self.client_address = client_address
        self.client_city = client_city
        self.client_state = client_state
        self.client_country = client_country
        self.client_type_id = client_type_id
        self.client_tax_id = client_tax_id
        self.client_tax_condition = client_tax_condition
        self.cae = cae if cae is not None else "N/A"
        self.cae_vto = cae_vto

    def __eq__(self, other):
        if not isinstance(other, ResponseDocumentDto):
            return False
        return self.__dict__ == other.__dict__

    def to_dict(self):
        def default_value(value, fallback):
            return value if value is not None else fallback

        return {
            "document_id": self.document_id,
            "client_id": self.client_id,
            "pos": self.pos,
            "document_type": self.document_type,
            "document_concept": self.document_concept,
            "number": self.number,
            "date": self.date.isoformat() if isinstance(self.date, datetime) else self.date,
            "date_serv_from": self.date_serv_from.isoformat() if isinstance(self.date_serv_from, datetime) else self.date_serv_from,
            "date_serv_to": self.date_serv_to.isoformat() if isinstance(self.date_serv_to,datetime) else self.date_serv_to,
            "expiration_date": self.expiration_date.isoformat() if isinstance(self.expiration_date, datetime) else self.expiration_date,
            "total_amount": self.total_amount,
            "taxable_amount": self.taxable_amount,
            "exempt_amount": self.exempt_amount,
            "no_grav_amount": self.no_grav_amount,
            "tributes_amount": self.tributes_amount,
            "tax_amount": self.tax_amount,
            "currency": self.currency,
            "exchange_rate": self.exchange_rate,
            "status": self.status,
            "client_name": self.client_name,
            "client_address": self.client_address,
            "client_city": self.client_city,
            "client_state": self.client_state,
            "client_country": self.client_country,
            "client_type_id": self.client_type_id,
            "client_tax_id": self.client_tax_id,
            "client_tax_condition": self.client_tax_condition,
            "cae": self.cae,
            "cae_vto":  self.cae_vto.isoformat() if isinstance(self.cae_vto, datetime) else self.cae_vto
        }

    def __str__(self):
        return (f"ResponseDocumentDto("
                f"document_id={self.document_id}, client_id={self.client_id}, pos={self.pos}, "
                f"document_type={self.document_type}, document_concept={self.document_concept}, "
                f"number={self.number}, date={self.date}, expiration_date={self.expiration_date}, "
                f"date_serv_from={self.date_serv_from},date_serv_to={self.date_serv_to},"
                f"total_amount={self.total_amount}, taxable_amount={self.taxable_amount}, "
                f"exempt_amount={self.exempt_amount}, no_grav_amount={self.no_grav_amount}, "
                f"tributes_amount={self.tributes_amount}, tax_amount={self.tax_amount}, "
                f"currency={self.currency}, exchange_rate={self.exchange_rate}, status={self.status}, "
                f"client_name={self.client_name}, client_address={self.client_address}, "
                f"client_city={self.client_city}, client_state={self.client_state}, "
                f"client_country={self.client_country}, client_type_id={self.client_type_id}, "
                f"client_tax_id={self.client_tax_id}, client_tax_condition={self.client_tax_condition}, "
                f"cae = {self.cae}, cae_vto={self.cae_vto}")

class ResponseDocumentDtoBuilder:
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
        self._no_grav_amount = None
        self._tributes_amount = None
        self._tax_amount = None
        self._currency = None
        self._exchange_rate = None
        self._status = None
        self._client_name = None
        self._client_address = None
        self._client_city = None
        self._client_state = None
        self._client_country = None
        self._client_type_id = None
        self._client_tax_id = None
        self._client_tax_condition = None
        self._cae = None
        self._cae_vto = None

    def document_id(self, document_id: int):
        self._document_id = document_id
        return self

    def client_id(self, client_id: int):
        self._client_id = client_id
        return self

    def pos(self, pos: int):
        self._pos = pos
        return self

    def document_type(self, document_type: str):
        self._document_type = document_type
        return self

    def document_concept(self, document_concept: str):
        self._document_concept = document_concept
        return self

    def number(self, number: int):
        self._number = number
        return self

    def date(self, date: datetime):
        self._date = date
        return self

    def date_serv_from(self, date_serv_from: datetime):
        self._date_serv_from = date_serv_from
        return self

    def date_serv_to(self, date_serv_to: datetime):
        self._date_serv_to = date_serv_to
        return self

    def expiration_date(self, expiration_date: datetime):
        self._expiration_date = expiration_date
        return self

    def total_amount(self, total_amount: float):
        self._total_amount = total_amount
        return self

    def taxable_amount(self, taxable_amount: float):
        self._taxable_amount = taxable_amount
        return self

    def exempt_amount(self, exempt_amount: float):
        self._exempt_amount = exempt_amount
        return self

    def no_grav_amount(self, no_grav_amount: float):
        self._no_grav_amount = no_grav_amount
        return self

    def tributes_amount(self, tributes_amount: float):
        self._tributes_amount = tributes_amount
        return self

    def tax_amount(self, tax_amount: float):
        self._tax_amount = tax_amount
        return self

    def currency(self, currency: str):
        self._currency = currency
        return self

    def exchange_rate(self, exchange_rate: float):
        self._exchange_rate = exchange_rate
        return self

    def status(self, status: str):
        self._status = status
        return self

    def client_name(self, client_name: str):
        self._client_name = client_name
        return self

    def client_address(self, client_address: str):
        self._client_address = client_address
        return self

    def client_city(self, client_city: str):
        self._client_city = client_city
        return self

    def client_state(self, client_state: str):
        self._client_state = client_state
        return self

    def client_country(self, client_country: str):
        self._client_country = client_country
        return self

    def client_type_id(self, client_type_id: str):
        self._client_type_id = client_type_id
        return self

    def client_tax_id(self, client_tax_id: str):
        self._client_tax_id = client_tax_id
        return self

    def client_tax_condition(self, client_tax_condition: str):
        self._client_tax_condition = client_tax_condition
        return self

    def cae(self,cae:str):
        self._cae = cae
        return self

    def cae_vto(self,cae_vto :datetime):
        self._cae_vto = cae_vto
        return self

    def build(self):
        return ResponseDocumentDto(
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
            no_grav_amount=self._no_grav_amount,
            tributes_amount=self._tributes_amount,
            tax_amount=self._tax_amount,
            currency=self._currency,
            exchange_rate=self._exchange_rate,
            status=self._status,
            client_name=self._client_name,
            client_address=self._client_address,
            client_city=self._client_city,
            client_state=self._client_state,
            client_country=self._client_country,
            client_type_id=self._client_type_id,
            client_tax_id=self._client_tax_id,
            client_tax_condition=self._client_tax_condition,
            cae=self._cae,
            cae_vto=self._cae_vto
        )



