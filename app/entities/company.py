from symbol import and_expr

from app.entities.enums.status import Status
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.typeId import TypeId


class Company:
    def __init__(self,company_id :int, company_name :str,company_address :str, company_city :str, company_state :str, company_country :str,
                 company_email :str, company_phone :str, company_tax_id :str, company_tax_condition :TaxCondition, company_type_id :TypeId, company_pos :int,
                 company_cert :bytes, company_key :bytes, company_status  :Status ):

        self.company_id :int = company_id
        self.company_name = company_name
        self.company_address :str = company_address
        self.company_city :str = company_city
        self.company_state :str = company_state
        self.company_country :str = company_country
        self.company_email :str = company_email
        self.company_phone :str = company_phone
        self.company_tax_id :str = company_tax_id
        self.company_type_id :TypeId = company_type_id
        self.company_tax_condition :TaxCondition = company_tax_condition
        self.company_pos :company_pos = company_pos
        self.company_cert: bytes = company_cert
        self.company_key :bytes = company_key
        self.company_status :Status = company_status


    def __str__(self):
        return (f"Empresa: {self.company_name}\n"
                f"Address: {self.company_address}\n"
                f"City: {self.company_city}\n"
                f"State: {self.company_city}\n"
                f"Country: {self.company_country}\n"
                f"Email: {self.company_email}\n"
                f"Phone: {self.company_phone}\n"
                f"Tipo id: {self.company_type_id}\n"
                f"Tax id: {self.company_tax_id}\n"
                f"Tax Condition: {self.company_tax_condition}\n"
                f"Status : {self.company_status}\n"
                f"Comapny_id : {self.company_id}\n"
                f"Company_pos : {self.company_pos}\n")


    def __eq__(self,other):
        if isinstance(other, Company):
             return(
             self.company_id == other.company_id and
             self.company_name == other.company_name and
             self.company_address == other.company_address and
             self.company_city == other.company_city and
             self.company_state == other.company_state and
             self.company_country == other.company_country and
             self.company_email == other.company_email and
             self.company_phone == other.company_phone and
             self.company_pos == other.company_pos
             )
        return False

    def to_dict(self):
        return {
            "company_id": self.company_id,
            "company_name": self.company_name,
            "company_address": self.company_address,
            "company_city":self.company_city,
            "company_state": self.company_state,
            "company_country": self.company_country,
            "company_email": self.company_email,
            "company_phone": self.company_phone,
            "company_type_id": self.company_type_id.get_type(),
            "company_tax_id": self.company_tax_id,
            "company_tax_condition":self.company_tax_condition.get_condition(),
            "company_cert": self.company_cert,
            "company_key": self.company_cert,
            "company_pos": self.company_pos,
            "company_status":self.company_status.get_value()
        }

class CompanyBuilder:
        def __init__(self):
            self._company_id = None
            self._company_name = None
            self._company_address = None
            self._company_city = None
            self._company_state = None
            self._company_country = None
            self._company_email = None
            self._company_phone = None
            self._company_type_id = None
            self._company_tax_id = None
            self._company_tax_condition = None
            self._company_pos = None
            self._company_cert = None
            self._company_key = None
            self._company_status = None

        def company_id(self, company_id):
            self._company_id: int = company_id
            return self

        def company_name(self,company_name):
            self._company_name = company_name
            return self

        def company_address(self,company_address):
            self._company_address = company_address
            return self

        def company_city(self,company_city):
            self._company_city = company_city
            return self

        def company_state(self,company_state):
            self._company_state = company_state
            return self

        def company_country(self,company_country):
            self._company_country = company_country
            return self

        def company_email(self,company_email):
            self._company_email = company_email
            return self

        def company_phone(self,company_phone):
            self._company_phone = company_phone
            return self

        def company_type_id(self,company_type_id):
            self._company_type_id = company_type_id
            return self

        def company_tax_id(self,company_tax_id):
            self._company_tax_id = company_tax_id
            return self

        def company_tax_condition(self, company_tax_condition):
            self._company_tax_condition = company_tax_condition
            return self

        def company_pos(self, company_pos):
            self._company_pos = company_pos
            return self

        def company_cert(self,company_cert):
            self._company_cert = company_cert
            return self

        def company_key(self,company_key):
            self._company_key = company_key
            return self

        def company_status(self,company_status):
            self._company_status = company_status
            return self

        def build(self):
            return Company(
                company_id=self._company_id,
                company_name=self._company_name,
                company_address=self._company_address,
                company_city=self._company_city,
                company_state=self._company_state,
                company_country=self._company_country,
                company_email=self._company_email,
                company_phone=self._company_phone,
                company_type_id=self._company_type_id,
                company_tax_id=self._company_tax_id,
                company_tax_condition=self._company_tax_condition,
                company_pos=self._company_pos,
                company_cert=self._company_cert,
                company_key=self._company_key,
                company_status=self._company_status
            )











