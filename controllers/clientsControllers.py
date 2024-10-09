from flask import Blueprint
from flask import request, jsonify
from dtos.clientDto import ClientDto
from dtos.responseClientDto import ResponseClientDto
from entities.enums.taxCondition import TaxCondition
from exceptions.wrapperExceptions import handle_exceptions
from entities.client import Client, ClientBuilder
from modules import clientService

clientsBp = Blueprint('clients', __name__)

@clientsBp.route("/", methods=['GET'])
@handle_exceptions
def get_all():
    clients = clientService.get_all()
    clients_data = [client.to_dict() for client in clients]
    response = ResponseClientDto(many=True).dump(clients_data)
    return jsonify(response), 200


@clientsBp.route("/<int:id>")
@handle_exceptions
def get_id(id):
    client = clientService.get_id(id)
    result: Client = ResponseClientDto().dump(client.to_dict())
    return jsonify(result)


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
                      .type_id(post_client_dto["type_id"])
                      .tax_id(post_client_dto["tax_id"])
                      .tax_condition(TaxCondition(post_client_dto["tax_condition"]))
                      .build())
    clientService.create(client)
    return jsonify({"message": "Client created successfully"}), 201


@clientsBp.route("/<int:id>", methods=['PUT'])
@handle_exceptions
def modify(id):
    modify_client_dto = ClientDto().load(request.json)
    client: Client = (ClientBuilder()
                      .name(modify_client_dto["name"])
                      .address(modify_client_dto["address"])
                      .city(modify_client_dto["city"])
                      .state(modify_client_dto["state"])
                      .country(modify_client_dto["country"])
                      .email(modify_client_dto["email"])
                      .phone(modify_client_dto["phone"])
                      .type_id(modify_client_dto["type_id"])
                      .tax_id(modify_client_dto["tax_id"])
                      .tax_condition(TaxCondition(modify_client_dto["tax_condition"]))
                      .build())
    clientService.modify(id,client)
    return jsonify({"message": "Client modfify successfully"}), 201


@clientsBp.route("/<int:id>", methods=['DELETE'])
@handle_exceptions
def delete(id):
    clientService.delete(id)
    return jsonify({"message": "Client deleted successfully"}), 201
