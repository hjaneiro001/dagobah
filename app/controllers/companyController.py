
from flask import Blueprint, request, jsonify

from app.dtos.requestCompanyDto import RequestCompanyDto
from app.dtos.requestCuentaArcaDto import RequestCuentaArcaDto
from app.dtos.responseCompanyDto import ResponseCompanyDto
from app.entities.company import Company, CompanyBuilder
from app.entities.cuentaArca import CuentaArca, CuentaArcaBuilder
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.typeId import TypeId
from app.exceptions.wrapperExceptions import handle_exceptions
from app.modules import companyService

companyBp = Blueprint('company', __name__)

@companyBp.route("/", methods=['POST'])
@handle_exceptions
def create():

    post_company_dto :RequestCompanyDto= RequestCompanyDto().load(request.json)

    company :Company = (CompanyBuilder()
            .company_name(post_company_dto["company_name"])
            .company_address(post_company_dto["company_address"])
            .company_city(post_company_dto["company_city"])
            .company_state(post_company_dto["company_state"])
            .company_country(post_company_dto["company_country"])
            .company_email(post_company_dto["company_email"])
            .company_phone(post_company_dto["company_phone"])
            .company_tax_id(post_company_dto["company_tax_id"])
            .company_type_id(TypeId.get_type_id(post_company_dto["company_type_id"]))
            .company_tax_condition(TaxCondition.get_tax_condition(post_company_dto["company_tax_condition"]))
            .build())

    company_id :int= companyService.create(company)

    return jsonify({"company_id" : company_id}), 201

@companyBp.route("/<int:id>", methods=['DELETE'])
@handle_exceptions
def delete(id: int):
    companyService.delete(id)
    return jsonify({"message": "Company deleted successfully"}), 200


@companyBp.route("/<int:id>", methods=['PUT'])
@handle_exceptions
def modify(id:int):

    post_company_dto :RequestCompanyDto= RequestCompanyDto().load(request.json)

    company :Company = (CompanyBuilder()
            .company_name(post_company_dto["company_name"])
            .company_address(post_company_dto["company_address"])
            .company_city(post_company_dto["company_city"])
            .company_state(post_company_dto["company_state"])
            .company_country(post_company_dto["company_country"])
            .company_email(post_company_dto["company_email"])
            .company_phone(post_company_dto["company_phone"])
            .company_tax_id(post_company_dto["company_tax_id"])
            .company_type_id(TypeId.get_type_id(post_company_dto["company_type_id"]))
            .company_tax_condition(TaxCondition.get_tax_condition(post_company_dto["company_tax_condition"]))
            .build())

    companyService.modify(id, company)
    return jsonify({"message": "Company modify successfully"}), 200


@companyBp.route("/<int:id>", methods=['GET'])
@handle_exceptions
def get_id(id :int):
    company: Company = companyService.get_id(id)
    response = ResponseCompanyDto().dump(company.to_dict())
    return jsonify(response), 200


@companyBp.route("/", methods=['GET'])
@handle_exceptions
def get_all():
    companies: list[Company] = companyService.get_all()

    if len(companies) == 0:
        return "", 204

    companies_data = [company.to_dict() for company in companies]
    response = ResponseCompanyDto(many=True).dump(companies_data)
    return jsonify(response), 200


@companyBp.route("/taxid/<taxId>", methods=['GET'])
@handle_exceptions
def get_tax_id(taxId :str):
    company: Company = companyService.get_tax_id(taxId)
    response = ResponseCompanyDto().dump(company.to_dict())
    return jsonify(response), 200


@companyBp.route("/certificado", methods=['PUT'])
@handle_exceptions
def create_certificado():

    post_cuenta_arca :RequestCuentaArcaDto = RequestCuentaArcaDto().load(request.json)

    cuentaArca :CuentaArca = (CuentaArcaBuilder()
                        .user(post_cuenta_arca["user"])
                        .password(post_cuenta_arca["password"])
                        .cert_name(post_cuenta_arca["cert_name"])
                        .company_id(post_cuenta_arca["company_id"])
                        .build())


    result = companyService.create_certificado(cuentaArca)

    return "",204

