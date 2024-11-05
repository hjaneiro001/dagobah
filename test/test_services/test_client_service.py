
from unittest.mock import patch
import unittest
import random

from app.entities.enums.status import Status
from app.exceptions.clientAlreadyExistsException import ClientAlreadyExistsException
from app.exceptions.clientNotFoundException import ClientNotFoundException
from app.services.clientService import ClientService
from test.mothers.clientMother import ClientMother

class TestClientService(unittest.TestCase):
    def setUp(self):
        self.mock_client_repository = patch('app.repositories.clientRepository.ClientRepository').start()
        self.client_service = ClientService(self.mock_client_repository)

    def tearDown(self):
        patch.stopall()

    @patch('app.repositories.clientRepository.ClientRepository.get_id')
    def test_get_id_success(self, mock_get_id):
        # Arrange
        mocked_client = ClientMother.normal_client(random.randint(1, 100))
        mock_get_id.return_value = mocked_client

        # Act
        result = self.client_service.get_id(mocked_client.pk_client)

        # Assert
        mock_get_id.assert_called_once_with(mocked_client.pk_client)
        self.assertEqual(result, mocked_client)

    @patch('app.repositories.clientRepository.ClientRepository.get_id')
    def test_get_id_not_found(self, mock_get_id):
        # Arrange
        mock_get_id.return_value = None

        # Act & Assert
        with self.assertRaises(ClientNotFoundException):
            self.client_service.get_id(1)


    @patch('app.repositories.clientRepository.ClientRepository.create')
    @patch('app.repositories.clientRepository.ClientRepository.get_tax_id')
    def test_create_client_success(self, mock_get_tax_id, mock_create):
        # Arrange
        mocked_client = ClientMother.normal_client(random.randint(1, 100))
        mock_get_tax_id.return_value = None
        mock_create.return_value = mocked_client.pk_client

        # Act
        client_id = self.client_service.create(mocked_client)

        # Assert
        mock_get_tax_id.assert_called_once_with(mocked_client.tax_id)
        mock_create.assert_called_once_with(mocked_client)
        self.assertEqual(client_id, mocked_client.pk_client)
        self.assertEqual(mocked_client.status, Status.ACTIVE)

    @patch('app.repositories.clientRepository.ClientRepository.create')
    @patch('app.repositories.clientRepository.ClientRepository.get_tax_id')
    def test_create_client_already_exists(self, mock_find_by_tax_id, mock_create):
        # Arrange
        mocked_client = ClientMother.normal_client(random.randint(1, 100))
        mock_find_by_tax_id.return_value = mocked_client

        # Act & Assert
        with self.assertRaises(ClientAlreadyExistsException):
            self.client_service.create(mocked_client)
        mock_create.assert_not_called()


    @patch('app.repositories.clientRepository.ClientRepository.get_all')
    def test_get_all_clients(self, mock_get_all):
        # Arrange
        mocked_client_a = ClientMother.normal_client(random.randint(1, 100))
        mocked_client_b = ClientMother.normal_client(random.randint(1, 100))
        mocked_client_list = [mocked_client_a, mocked_client_b]
        mock_get_all.return_value = mocked_client_list

        # Act
        result = self.client_service.get_all()

        # Assert
        mock_get_all.assert_called_once()
        self.assertEqual(result, mocked_client_list)

    @patch('app.repositories.clientRepository.ClientRepository.get_tax_id')
    @patch('app.repositories.clientRepository.ClientRepository.save')
    @patch('app.repositories.clientRepository.ClientRepository.get_id')
    def test_modify_client_success(self, mock_get_id, mock_save,mock_get_tax_id):
        # Arrange
        id_to_modify = random.randint(1, 100)
        client_to_modify = ClientMother.normal_client(id_to_modify)
        client_updated = ClientMother.normal_client(id_to_modify)

        mock_get_id.return_value = client_to_modify
        mock_get_tax_id.return_value = client_to_modify

        # Act
        self.client_service.modify(id_to_modify, client_updated)

        # Assert
        mock_get_id.assert_called_once_with(id_to_modify)
        mock_save.assert_called_once_with(client_updated)
        self.assertEqual(client_updated.pk_client, client_to_modify.pk_client)
        self.assertEqual(client_updated.status, client_to_modify.status)


    @patch('app.repositories.clientRepository.ClientRepository.get_id')
    def test_modify_client_not_found(self, mock_get_id):
        # Arrange
        id_to_modify = random.randint(1, 100)
        client_updated = ClientMother.normal_client(id_to_modify)

        mock_get_id.return_value = None

        # Act & Assert
        with self.assertRaises(ClientNotFoundException):
            self.client_service.modify(id_to_modify, client_updated)
        self.mock_client_repository.save.assert_not_called()


    @patch('app.repositories.clientRepository.ClientRepository.save')
    @patch('app.repositories.clientRepository.ClientRepository.get_id')
    def test_delete_client_success(self, mock_get_id, mock_save):
        # Arrange
        id_to_delete = random.randint(1, 100)
        client_to_delete = ClientMother.normal_client(id_to_delete)

        mock_get_id.return_value = client_to_delete

        # Act
        self.client_service.delete(id_to_delete)

        # Assert
        mock_get_id.assert_called_once_with(id_to_delete)
        mock_save.assert_called_once_with(client_to_delete)
        self.assertEqual(client_to_delete.status, Status.INACTIVE)

    @patch('app.repositories.clientRepository.ClientRepository.get_id')
    def test_delete_client_not_found(self, mock_get_id):
        # Arrange
        id_to_delete = random.randint(1, 100)

        mock_get_id.return_value = None

        # Act & Assert
        with self.assertRaises(ClientNotFoundException):
            self.client_service.delete(id_to_delete)
        self.mock_client_repository.save.assert_not_called()
