import os

from app.entities.company import Company, CompanyBuilder
from app.entities.cuentaArca import CuentaArca
from app.entities.enums.status import Status
from app.exceptions.companyTaxIdAlreadyExistsException import CompanyTaxIdAlreadyExistsException
from app.exceptions.companytAlreadytExistsException import CompanyAlreadyExistsException
from app.exceptions.companytNotFoundException import CompanyNotFoundException


class CompanyService:

    def __init__(self, company_repository,sdk_afip_repository):
        self.company_repository = company_repository
        self.sdk_afip_repository = sdk_afip_repository

    def create(self, company :Company):

        company.company_status = Status.ACTIVE
        if self.company_repository.get_tax_id(company.company_tax_id):
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

    def create_certificado(self,cuentaArca :CuentaArca ):

        company = self.company_repository.get_id(cuentaArca.company_id)
        cert = self.sdk_afip_repository.create_certificado(company,cuentaArca)
        return self.company_repository.save_certificado(cuentaArca.company_id,cert["cert"],cert["key"])


    def autorizar_certificado(self, cuentaArca: CuentaArca):
        company = self.company_repository.get_id(cuentaArca.company_id)
        self.sdk_afip_repository.autorizar_certificado(company, cuentaArca)