from entities.client import Client, ClientBuilder
import pymysql.cursors

from entities.enums.clientStatus import ClientStatus
from entities.enums.taxCondition import TaxCondition
from entities.enums.typeId import TypeId


class ClientRepository:

    def __init__(self, connection):
        self.conn = connection


    def create(self, client : Client):
            sql: str = """
                INSERT INTO clients (client_name, client_address, client_city, client_state, client_country, client_email, client_phone, client_type_id, client_tax_id, client_tax_condition, client_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                client.name, client.address, client.city, client.state, client.country,
                client.email, client.phone, client.type_id.value, client.tax_id,
                client.tax_condition.value, client.status.value
            )

            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()


    def find_by_tax_id(self, taxid: str):
            sql: str = "SELECT * FROM clients WHERE client_tax_id = %s AND client_status = 'ACTIVE'"
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, (taxid,))
            row = cursor.fetchone()
            return row


    def save(self,client: Client):
        sql: str = """
                UPDATE clients
                SET client_name = %s, client_address = %s, client_city = %s, client_state = %s,
                    client_country = %s, client_email = %s, client_phone = %s, client_type_id = %s,
                    client_tax_id = %s, client_tax_condition = %s, client_status = %s
                WHERE client_id = %s
            """

        values = (
            client.name, client.address, client.city, client.state, client.country,
            client.email, client.phone, client.type_id.value, client.tax_id,
            client.tax_condition.value, client.status.value, client.pk_client
        )

        cursor = self.conn.cursor()
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()


    def get_id(self, id: int):
        sql = "SELECT * FROM clients WHERE client_id = %s AND client_status = 'ACTIVE'"
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
                .type_id(TypeId(row.get('client_type_id')))
                .tax_id(row.get('client_tax_id'))
                .tax_condition(TaxCondition(row.get('client_tax_condition')))
                .status(ClientStatus(row.get('client_status')))
                .build())

        return client

    def get_all(self):

            sql = "SELECT * FROM clients WHERE client_status = 'ACTIVE'"
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
                          .type_id(TypeId(row.get('client_type_id')))
                          .tax_id(row.get('client_tax_id'))
                          .tax_condition(TaxCondition(row.get('client_tax_condition')))
                          .status(row.get('client_status'))
                          .build())

                clients.append(client)

            return clients

    def delete(self, id: int):

        sql: str = """
                   UPDATE clients
                   SET client_status = "INACTIVE"
                   WHERE client_id = %s
               """

        cursor = self.conn.cursor()
        cursor.execute(sql, id)
        self.conn.commit()
        cursor.close()



