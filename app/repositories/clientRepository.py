from app.entities.client import Client, ClientBuilder
import pymysql.cursors

from app.entities.enums.status import Status

from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.clientType import ClientType
from app.entities.enums.typeId import TypeId

class ClientRepository:

    def __init__(self, connection):
        self.conn = connection

    def create(self, client : Client):

            sql: str = """
                INSERT INTO clients (client_name, client_address, client_city, client_state, client_country, client_email, client_phone, client_type_id, client_tax_id, client_tax_condition,client_type, client_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                client.name, client.address, client.city, client.state, client.country,
                client.email, client.phone, client.type_id.get_type(), client.tax_id,
                client.tax_condition.get_condition() ,client.client_type.get_type(), client.status.get_value()
            )

            cursor = self.conn.cursor()
            cursor.execute(sql, values)

            client_id = cursor.lastrowid

            self.conn.commit()

            return client_id

    def get_tax_id(self, taxid: str):

            sql: str = f"SELECT * FROM clients WHERE client_tax_id = %s AND client_status = '{Status.ACTIVE.get_value()}'"
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, (taxid,))
            row = cursor.fetchone()

            if row is None:
                return None

            client = (ClientBuilder()
                      .pk_client(row.get('client_id'))
                      .name(row.get('client_name'))
                      .address(row.get('client_address'))
                      .city(row.get('client_city'))
                      .state(row.get('client_state'))
                      .country(row.get('client_country'))
                      .email(row.get('client_email'))
                      .phone(row.get('client_phone'))
                      .type_id(TypeId.get_type_id(row.get('client_type_id')))
                      .tax_id(row.get('client_tax_id'))
                      .tax_condition(TaxCondition.get_tax_condition(row.get('client_tax_condition')))
                      .client_type(ClientType.get_clienttype(row.get('client_type')))
                      .status(Status.get_status(row.get('client_status')))
                      .build())

            return client

    def save(self,client: Client):

        sql: str = """
                UPDATE clients
                SET client_name = %s, client_address = %s, client_city = %s, client_state = %s,
                    client_country = %s, client_email = %s, client_phone = %s, client_type_id = %s,
                    client_tax_id = %s, client_tax_condition = %s, client_type = %s, client_status = %s
                WHERE client_id = %s
            """

        values = (
            client.name, client.address, client.city, client.state, client.country,
            client.email, client.phone, client.type_id.get_type(), client.tax_id,
            client.tax_condition.get_condition() , client.client_type.get_type(), client.status.get_value(), client.pk_client
        )

        cursor = self.conn.cursor()
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()


    def get_id(self, id: int):
        sql = f"SELECT * FROM clients WHERE client_id = %s AND client_status = '{Status.ACTIVE.get_value()}'"
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, (id,))
        row = cursor.fetchone()

        if row is None:
            return None

        client = (ClientBuilder()
                .pk_client(row.get('client_id'))
                .name(row.get('client_name'))
                .address(row.get('client_address'))
                .city(row.get('client_city'))
                .state(row.get('client_state'))
                .country(row.get('client_country'))
                .email(row.get('client_email'))
                .phone(row.get('client_phone'))
                .type_id(TypeId.get_type_id(row.get('client_type_id')))
                .tax_id(row.get('client_tax_id'))
                .tax_condition(TaxCondition.get_tax_condition(row.get('client_tax_condition')))
                .client_type(ClientType.get_clienttype(row.get('client_type')))
                .status(Status.get_status(row.get('client_status')))
                .build())

        return client

    def get_all(self):

            sql = f"SELECT * FROM clients WHERE client_status = '{Status.ACTIVE.get_value()}'"
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rows = cursor.fetchall()

            clients:  list[Client] = []

            for row in rows:
                client = (ClientBuilder()
                          .pk_client(row.get('client_id'))
                          .name(row.get('client_name'))
                          .address(row.get('client_address'))
                          .city(row.get('client_city'))
                          .state(row.get('client_state'))
                          .country(row.get('client_country'))
                          .email(row.get('client_email'))
                          .phone(row.get('client_phone'))
                          .type_id(TypeId.get_type_id(row.get('client_type_id')))
                          .tax_id(row.get('client_tax_id'))
                          .tax_condition(TaxCondition.get_tax_condition(row.get('client_tax_condition')))
                          .client_type(ClientType.get_clienttype(row.get('client_type')))
                          .status(Status.get_status(row.get('client_status')))
                          .build())

                clients.append(client)

            return clients




