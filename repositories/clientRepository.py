from entities.client import Client

class ClientRepository:
    def __init__(self):
        pass

    def save(self, client):
        print(client)
        return

    def find_client_by_tax_id(self, taxID):
        return

    def get_all(self):

        client1 = Client(
            pk_client=1,
            name="John Doe",
            address="123 Fake Street",
            city="Springfield",
            state="Illinois",
            country="USA",
            email="john.doe@fakemail.com",
            phone="+1 555 123 4567",
            type_id=1,
            tax_id="US123456789",
            tax_condition="Individual",
            status="Active"
        )

        client2 = Client(
            pk_client=2,
            name="Jane Smith",
            address="456 Mock Ave",
            city="Metropolis",
            state="New York",
            country="USA",
            email="jane.smith@mockmail.com",
            phone="+1 555 987 6543",
            type_id=2,
            tax_id="US987654321",
            tax_condition="Company",
            status="Active"
        )

        clients = [client1, client2]

        return clients

    def get_id(self, id):

        client = Client(
            pk_client=1,
            name="John Doe",
            address="123 Fake Street",
            city="Springfield",
            state="Illinois",
            country="USA",
            email="john.doe@fakemail.com",
            phone="+1 555 123 4567",
            type_id=1,
            tax_id="US123456789",
            tax_condition="Individual",
            status="Active"
        )

        return client
