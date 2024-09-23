from exceptions.clientAlreadyExistsException import ClientAlreadyExistsException
from repositories.clientRepository import ClientRepository

class ClientService:
    def __init__(self):
        self.clientRepository = ClientRepository

    def save(self, postClientDto):
        if not self.clientRepository.findClientByTaxId(postClientDto.taxID):
            self.clientRepository.save(postClientDto) 
        else:
            raise ClientAlreadyExistsException
