from entities.client import Client
from exceptions.clientAlreadyExistsException import ClientAlreadyExistsException
from exceptions.clientNotFoundException import ClientNotFoundException


class ClientService:
    def __init__(self, client_repository):
        self.client_repository = client_repository

    def save(self, client: Client):
        if not self.client_repository.find_client_by_tax_id(client.tax_id):
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
