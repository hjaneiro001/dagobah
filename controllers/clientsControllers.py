from flask import Blueprint
from flask import request, jsonify
from dtos.postClientDto import PostClientDto
from dtos.responseClientDto import ResponseClientDto
from exceptions.wrapperExceptions import handle_exceptions
from services.clientService import ClientService
from repositories.clientRepository import  ClientRepository
from entities.client import Client

clientsBp = Blueprint('clients', __name__)
clientService = ClientService(ClientRepository())

@clientsBp.route("/", methods=['POST'])
@handle_exceptions
def create():
    post_client_dto = PostClientDto().load(request.json)
    client = Client(pk_client=post_client_dto["pk_client"],
                    name=post_client_dto["name"],
                    address=post_client_dto["address"],
                    city=post_client_dto["city"],
                    state=post_client_dto["state"],
                    country=post_client_dto["country"],
                    email=post_client_dto["email"],
                    phone=post_client_dto["phone"],
                    type_id=post_client_dto["type_id"],
                    tax_id=post_client_dto["tax_id"],
                    tax_condition=post_client_dto["tax_condition"],
                    status=post_client_dto["status"]
                    )
    clientService.save(client)
    return jsonify({"message": "User created successfully"}), 201

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
    result = ResponseClientDto().dump(client)
    return jsonify(result)


@clientsBp.route("/", methods=['PUT'])
@handle_exceptions
def modify():
    post_client_dto = PostClientDto.load(request.json)
    client = Client(pk_client=post_client_dto["pk_client"],
                    name=post_client_dto["name"],
                    address=post_client_dto["address"],
                    city=post_client_dto["city"],
                    state=post_client_dto["state"],
                    country=post_client_dto["country"],
                    email=post_client_dto["email"],
                    phone=post_client_dto["phone"],
                    type_id=post_client_dto["type_id"],
                    tax_id=post_client_dto["tax_id"],
                    tax_condition=post_client_dto["tax_condition"],
                    status=post_client_dto["status"]
                    )
    clientService.save(client)
    return jsonify({"message": "User modfify successfully"}), 201
