from flask import Blueprint
from flask import request, jsonify
from app.dtos.clientDto import ClientDto
from app.dtos.responseClientDto import ResponseClientDto
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.clientType import ClientType
from app.entities.enums.typeId import TypeId
from app.exceptions.wrapperExceptions import handle_exceptions
from app.entities.client import Client, ClientBuilder
from app.modules import clientService

clientsBp = Blueprint('clients', __name__)

@clientsBp.route("/", methods=['GET'])
@handle_exceptions
def get_all():
    clients :list[Client]= clientService.get_all()
    clients_data = [client.to_dict() for client in clients]
    response = ResponseClientDto(many=True).dump(clients_data)
    return jsonify(response), 200


@clientsBp.route("/<int:id>")
@handle_exceptions
def get_id(id :int):
    client: Client = clientService.get_id(id)
    result = ResponseClientDto().dump(client.to_dict())
    return jsonify(result), 200

@clientsBp.route("/cuit/<int:taxId>")
@handle_exceptions
def get_taxId(taxId :int):
    client: Client = clientService.get_taxId(taxId)
    result = ResponseClientDto().dump(client.to_dict())
    return jsonify(result), 200


@clientsBp.route("/", methods=['POST'])
@handle_exceptions
def create():
    post_client_dto = ClientDto().load(request.json)

    client: Client = (ClientBuilder()
                        .name(post_client_dto["name"])
                        .address(post_client_dto["address"])
                        .city(post_client_dto["city"])
                        .state(post_client_dto["state"])
                        .country(post_client_dto["country"])
                        .email(post_client_dto["email"])
                        .phone(post_client_dto["phone"])
                        .type_id(TypeId.get_type_id(post_client_dto["type_id"]))
                        .tax_id(post_client_dto["tax_id"])
                        .tax_condition(TaxCondition.get_tax_condition(post_client_dto["tax_condition"]))
                        .client_type(ClientType.get_clienttype(post_client_dto["client_type"]))
                        .build())

    client_id: int = clientService.create(client)
    return jsonify({"client_id" : client_id}), 201

@clientsBp.route("/<int:id>", methods=['PUT'])
@handle_exceptions
def modify(id :int):
    modify_client_dto = ClientDto().load(request.json)
    client: Client = (ClientBuilder()
                      .name(modify_client_dto["name"])
                      .address(modify_client_dto["address"])
                      .city(modify_client_dto["city"])
                      .state(modify_client_dto["state"])
                      .country(modify_client_dto["country"])
                      .email(modify_client_dto["email"])
                      .phone(modify_client_dto["phone"])
                      .type_id(TypeId.get_type_id(modify_client_dto["type_id"]))
                      .tax_id(modify_client_dto["tax_id"])
                      .tax_condition(TaxCondition.get_tax_condition(modify_client_dto["tax_condition"]))
                      .client_type(ClientType.get_clienttype(modify_client_dto["client_type"]))
                      .build())

    clientService.modify(id, client)
    return jsonify({"message": "Client modify successfully"}), 200


@clientsBp.route("/<int:id>", methods=['DELETE'])
@handle_exceptions
def delete(id: int):
    clientService.delete(id)
    return jsonify({"message": "Client deleted successfully"}), 200
