import unittest
from unittest.mock import MagicMock, ANY

from sqlalchemy.engine.mock import MockConnection

from app.entities.client import Client, ClientBuilder
from app.repositories.clientRepository import ClientRepository
from test.mothers.clientMother import ClientMother


class ClientRepositoryTestCase(unittest.TestCase):

    def test_get_all(self):

        expected_sql :str = "SELECT * FROM clients WHERE client_status = 'ACTIVE'"
        expected_client: Client = ClientMother.normal_client(1)

        expected_db_response = [{
            'client_id': expected_client.pk_client,
            'client_name': expected_client.name,
            'client_address': expected_client.address,
            'client_city': expected_client.city,
            'client_state': expected_client.state,
            'client_country': expected_client.country,
            'client_email': expected_client.email,
            'client_phone': expected_client.phone,
            'client_type_id': expected_client.type_id.get_type(),
            'client_tax_id': expected_client.tax_id,
            'client_tax_condition': expected_client.tax_condition.value,
            'client_type': expected_client.client_type.get_type(),
            'client_status': expected_client.status.value
        }]

        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = expected_db_response

        client_repository = ClientRepository(mock_connection)

        #act
        clients = client_repository.get_all()

        #asserts
        assert clients[0] == expected_client
        mock_cursor.execute.assert_called_with(expected_sql)

    def test_get_id(self):
        expected_sql: str = "SELECT * FROM clients WHERE client_id = %s AND client_status = 'ACTIVE'"
        expected_client: Client = ClientMother.normal_client(1)

        expected_db_response = {
            'client_id': expected_client.pk_client,
            'client_name': expected_client.name,
            'client_address': expected_client.address,
            'client_city': expected_client.city,
            'client_state': expected_client.state,
            'client_country': expected_client.country,
            'client_email': expected_client.email,
            'client_phone': expected_client.phone,
            'client_type_id': expected_client.type_id.get_type(),
            'client_tax_id': expected_client.tax_id,
            'client_tax_condition': expected_client.tax_condition.value,
            'client_type': expected_client.client_type.get_type(),
            'client_status': expected_client.status.value
        }

        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = expected_db_response

        client_repository = ClientRepository(mock_connection)

        # act
        clients = client_repository.get_id(expected_client.pk_client)

        # asserts
        assert clients == expected_client
        mock_cursor.execute.assert_called_with(expected_sql, (expected_client.pk_client,))


    def test_create(self):

        expected_client_id :int = 1
        client_to_create :Client = ClientMother.normal_client(1)

        expected_sql :str = """
                INSERT INTO clients (client_name, client_address, client_city, client_state, client_country, client_email, client_phone, client_type_id, client_tax_id, client_tax_condition,client_type, client_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

        expected_values = (
            client_to_create.name,
            client_to_create.address,
            client_to_create.city,
            client_to_create.state,
            client_to_create.country,
            client_to_create.email,
            client_to_create.phone,
            client_to_create.type_id.get_type(),
            client_to_create.tax_id,
            client_to_create.tax_condition.value,
            client_to_create.client_type.get_type(),
            client_to_create.status.value
        )

        # Mock objects
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.lastrowid = expected_client_id
        client_repository = ClientRepository(mock_connection)

        # Act
        pk_new_client = client_repository.create(client_to_create)

        assert pk_new_client == expected_client_id
        mock_cursor.execute.assert_called_with(expected_sql, expected_values)

    def test_save(self):

        client_to_modify = ClientMother.normal_client(1)

        expected_values = (
            client_to_modify.name,
            client_to_modify.address,
            client_to_modify.city,
            client_to_modify.state,
            client_to_modify.country,
            client_to_modify.email,
            client_to_modify.phone,
            client_to_modify.type_id.get_type(),
            client_to_modify.tax_id,
            client_to_modify.tax_condition.value,
            client_to_modify.client_type.get_type(),
            client_to_modify.status.value,
            client_to_modify.pk_client
        )


        # Mock objects
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        client_repository = ClientRepository(mock_connection)

        # Act
        client_repository.save(client_to_modify)

        # Assert
        mock_cursor.execute.assert_called_with(ANY, expected_values)
