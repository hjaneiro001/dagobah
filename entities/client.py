from entities.enums.clientStatus import ClientStatus
from entities.enums.taxCondition import TaxCondition


class Client:
    def __init__(self, pk_client :int, name :str, address :str, city :str, state :str, country :str, email :str, phone :str, type_id :str, tax_id :str, tax_condition :TaxCondition, status :ClientStatus):
        self.pk_client :int = pk_client
        self.name :str = name
        self.address :str= address
        self.city :str= city
        self.state :str= state
        self.country :str= country
        self.email :str= email
        self.phone :str= phone
        self.type_id :str= type_id
        self.tax_id :str= tax_id
        self.tax_condition :TaxCondition = tax_condition
        self.status :ClientStatus= status

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Country: {self.country}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n"
                f"Phone: {self.type_id}\n"
                f"Tax ID: {self.tax_id}\n"
                f"Tax Condition: {self.tax_condition.value}")

    def to_dict(self):
        return {
            "pk_client": self.pk_client,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "email": self.email,
            "phone": self.phone,
            "type_id": self.type_id,
            "tax_id": self.tax_id,
            "tax_condition": self.tax_condition.value,
            "status": self.status
        }

class ClientBuilder:
    def __init__(self):
        self._pk_client = None
        self._name = None
        self._address = None
        self._city = None
        self._state = None
        self._country = None
        self._email = None
        self._phone = None
        self._type_id = None
        self._tax_id = None
        self._tax_condition = None
        self._status = None

    def pk_client(self, pk_client):
        self._pk_client :int = pk_client
        return self

    def name(self, name):
        self._name :str = name
        return self

    def address(self, address):
        self._address :str = address
        return self

    def city(self, city):
        self._city :str = city
        return self

    def state(self, state):
        self._state :str = state
        return self

    def country(self, country):
        self._country :str = country
        return self

    def email(self, email):
        self._email :str = email
        return self

    def phone(self, phone):
        self._phone :str = phone
        return self

    def type_id(self, type_id):
        self._type_id :str = type_id
        return self

    def tax_id(self, tax_id):
        self._tax_id :str = tax_id
        return self

    def tax_condition(self, tax_condition :TaxCondition):
        self._tax_condition :TaxCondition = tax_condition
        return self

    def status(self, status :ClientStatus):
        self._status :ClientStatus = status
        return self

    def build(self):
        return Client(
            pk_client =self._pk_client,
            name=self._name,
            address=self._address,
            city=self._city,
            state=self._state,
            country=self._country,
            email=self._email,
            phone=self._phone,
            type_id=self._type_id,
            tax_id=self._tax_id,
            tax_condition=self._tax_condition,
            status=self._status
        )