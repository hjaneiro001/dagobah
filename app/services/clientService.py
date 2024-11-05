from app.entities.client import Client
from app.entities.enums.status import Status
from app.exceptions.clientAlreadyExistsException import ClientAlreadyExistsException
from app.exceptions.clientNotFoundException import ClientNotFoundException
from app.exceptions.clientTaxIdAlreadyExistsException import ClientTaxIdAlreadyExistsException


class ClientService:
    def __init__(self, client_repository):
        self.client_repository = client_repository

    def create(self, client: Client):
        if self.client_repository.get_tax_id(client.tax_id):
            raise ClientAlreadyExistsException
        client.status = Status.ACTIVE
        client_id :int = self.client_repository.create(client)
        return client_id

    def get_all(self):
        return self.client_repository.get_all()

    def get_id(self, id):
        client: Client = self.client_repository.get_id(id)
        if client is None:
            raise ClientNotFoundException
        return client

    def get_taxId(self, taxId):
        client: Client = self.client_repository.get_tax_id(taxId)
        if client is None:
            raise ClientNotFoundException
        return client

    def modify(self,id: int,client: Client):
        client_to_modify: Client = self.client_repository.get_id(id)
        if client_to_modify is None:
            raise ClientNotFoundException

        existing_client: Client = self.client_repository.get_tax_id(client.tax_id)
        if existing_client and existing_client.pk_client != id:
            raise ClientTaxIdAlreadyExistsException

        client.pk_client = client_to_modify.pk_client
        client.status = Status.ACTIVE
        self.client_repository.save(client)
        return

    def delete(self, id):
        client: Client = self.client_repository.get_id(id)
        if client is None:
            raise ClientNotFoundException
        client.status = Status.INACTIVE
        self.client_repository.save(client)
        return
