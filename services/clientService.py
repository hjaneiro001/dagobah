from entities.client import Client
from exceptions.clientAlreadyExistsException import ClientAlreadyExistsException
from exceptions.clientNotFoundException import ClientNotFoundException


class ClientService:
    def __init__(self, client_repository):
        self.client_repository = client_repository

    def create(self, client: Client):
        if not self.client_repository.find_client_by_tax_id(client.tax_id):
            client.status = "A"
            self.client_repository.save(client)
        else:
            raise ClientAlreadyExistsException

    def get_all(self):
        return self.client_repository.get_all()

    def get_id(self, id):
        client = self.client_repository.get_id(id)
        if client is None:
            raise ClientNotFoundException
        return client

    def modify(self,id,client: Client):
        client_to_modify: Client = self.client_repository.get_id(id)
        if client_to_modify is None:
            raise ClientNotFoundException
        client.status = client_to_modify.status
        self.client_repository.save(client)
        return

    def delete(self, id):
        client = self.client_repository.get_id(id)
        if client is None:
            raise ClientNotFoundException
        client.status = "I"
        self.client_repository.save(client)
        return client
