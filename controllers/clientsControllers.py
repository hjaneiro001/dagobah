from flask import Blueprint
from flask import request, jsonify
from dtos.clients import PostClientDto
from exceptions.wrapperExceptions import handle_exceptions
from services.clientService import ClientService


clientsBp = Blueprint('clients', __name__)
clientService = ClientService()

@clientsBp.route("/", methods=['POST'])
@handle_exceptions
def create():
    postClientDto = PostClientDto().load(request.json)
    clientService.save(postClientDto)
    return jsonify({"message": "User created successfully"}), 201