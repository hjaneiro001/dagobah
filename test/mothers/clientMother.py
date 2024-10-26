from app.entities.client import Client, ClientBuilder
from app.entities.enums.status import Status
from app.entities.enums.clientType import ClientType
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.typeId import TypeId

class ClientMother:
    def normal_client(id: int):
        client: Client = (ClientBuilder()
                          .pk_client(id)
                          .name("Natalia Natalia")
                          .address("Fake street 123")
                          .city("Springfield")
                          .state("Arizona")
                          .country("Fake Country")
                          .email("NataliaNatalia@Fakemail.com")
                          .phone("123456789")
                          .type_id(TypeId.CUIT)
                          .tax_id("123123123")
                          .tax_condition(TaxCondition.RI)
                          .client_type(ClientType.CLIENTE)
                          .status(Status.ACTIVE)
                          .build())
        return client