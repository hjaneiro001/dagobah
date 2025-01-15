import os

from app.entities.company import Company
from app.entities.enums.status import Status
from app.exceptions.companyTaxIdAlreadyExistsException import CompanyTaxIdAlreadyExistsException
from app.exceptions.companytAlreadytExistsException import CompanyAlreadyExistsException
from app.exceptions.companytNotFoundException import CompanyNotFoundException


class CompanyService:

    def __init__(self, company_repository ):
        self.company_repository = company_repository

    def create(self, company :Company):

        company.company_status = Status.ACTIVE
        company :Company = self.company_repository.get_tax_id(company.company_tax_id)
        if company:
            raise CompanyAlreadyExistsException
        company_id = self.company_repository.create(company)

        return  company_id

    def delete(self, id):
        company: Company = self.company_repository.get_id(id)
        if company is None:
            raise CompanyNotFoundException
        company.company_status = Status.INACTIVE
        self.company_repository.save(company)
        return

    def modify(self, id: int, company: Company):
        company_to_modify: Company = self.company_repository.get_id(id)
        if company_to_modify is None:
            raise CompanyNotFoundException

        existing_company: Company = self.company_repository.get_tax_id(company.company_tax_id)
        if existing_company and existing_company.company_id != id:
            raise CompanyTaxIdAlreadyExistsException

        company.company_id = company_to_modify.company_id
        company.company_status = Status.ACTIVE

        self.company_repository.save(company)

        return

    def get_tax_id(self,taxId :str):

        company_return :Company = self.company_repository.get_tax_id(taxId)

        if company_return is None:
            raise CompanyNotFoundException
        return company_return


    def get_id(self,id :int):

        company :Company = self.company_repository.get_id(id)

        if company is None:
            raise CompanyNotFoundException
        return company

    def get_all(self):

        companies = self.company_repository.get_all()

        return companies


    def create_certificado(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))

        cert_path = os.path.join(current_dir, "certificado.crt")

        cert = open(cert_path).read()

        return self.company_repository.save_certificado(1,cert)


    def create_key(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        key_path = os.path.join(current_dir, "key.key")

        key = open(key_path).read()

        return self.company_repository.save_key(1,key)





