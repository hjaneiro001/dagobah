import unittest
from unittest.mock import patch, MagicMock, ANY
from app.entities.client import Client
from app.repositories.clientRepository import ClientRepository
from test.mothers.clientMother import ClientMother
from app.entities.enums.status import Status



class ClientRepositoryTestCase(unittest.TestCase):

    @patch("app.repositories.clientRepository.ConnectionManager")
    @patch("app.repositories.clientRepository.CursorManager")
    def test_get_all(self, mock_cursor_manager, mock_connection_manager):

        expected_sql = f"SELECT * FROM clients WHERE client_status = '{Status.ACTIVE.get_value()}'"
        expected_client = ClientMother.normal_client(1)

        mock_rows = [{
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
            'client_tax_condition': expected_client.tax_condition.get_condition(),
            'client_type': expected_client.client_type.get_type(),
            'client_status': expected_client.status.ACTIVE.get_value()
        }]

        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = mock_rows
        mock_cursor_manager.return_value.__enter__.return_value = mock_cursor

        client_repository = ClientRepository(pool_connection="mock_pool")

        # Act
        clients = client_repository.get_all()

        # Asserts
        assert clients[0] == expected_client
        mock_cursor.execute.assert_called_once_with(expected_sql)

    @patch("app.repositories.clientRepository.ConnectionManager")
    @patch("app.repositories.clientRepository.CursorManager")
    def test_get_id(self, mock_cursor_manager, mock_connection_manager):

        expected_sql = f"SELECT * FROM clients WHERE client_id = %s AND client_status = '{Status.ACTIVE.get_value()}'"
        expected_client = ClientMother.normal_client(1)

        mock_row = {
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
            'client_tax_condition': expected_client.tax_condition.get_condition(),
            'client_type': expected_client.client_type.get_type(),
            'client_status': expected_client.status.ACTIVE.get_value()
        }

        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = mock_row
        mock_cursor_manager.return_value.__enter__.return_value = mock_cursor

        client_repository = ClientRepository(pool_connection="mock_pool")

        client = client_repository.get_id(expected_client.pk_client)

        assert client == expected_client
        mock_cursor.execute.assert_called_once_with(expected_sql, (expected_client.pk_client,))


    @patch("app.repositories.clientRepository.ConnectionManager")
    @patch("app.repositories.clientRepository.CursorManager")
    def test_save(self, mock_cursor_manager, mock_connection_manager):

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
            client_to_modify.tax_condition.get_condition(),
            client_to_modify.client_type.get_type(),
            client_to_modify.status.ACTIVE.get_value(),
            client_to_modify.pk_client
        )

        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        mock_connection_manager.return_value.__enter__.return_value = mock_connection
        mock_cursor_manager.return_value.__enter__.return_value = mock_cursor

        client_repository = ClientRepository(pool_connection="mock_pool")

        client_repository.save(client_to_modify)

        mock_cursor.execute.assert_called_once_with(
            ANY,
            expected_values
        )

