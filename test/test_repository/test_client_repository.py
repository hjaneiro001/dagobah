import unittest
from unittest.mock import Mock

from app.repositories.clientRepository import ClientRepository
from test.mothers.clientMother import ClientMother

class ClientRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.repository = ClientRepository(None)

    def mock_conn_create(self, return_id):
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_cursor.lastrowid = return_id
        mock_cursor.execute.return_value = None
        mock_conn.cursor.return_value = mock_cursor
        mock_conn.commit.return_value = None
        return mock_conn

    def mock_conn_update(self):
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_conn.cursor.return_value = mock_cursor
        mock_conn.commit.return_value = None
        return mock_conn

    def mock_conn_fetch_one(self, return_object):
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchone.return_value = return_object
        mock_conn.cursor.return_value = mock_cursor
        return mock_conn

    def test_create(self):
        self.repository.conn = self.mock_conn_create(1)
        self.assertEqual(1, self.repository.create(ClientMother.normal_client(1)))

    def test_find_by_tax_id(self):
        client = ClientMother.normal_client(1)
        self.repository.conn = self.mock_conn_fetch_one(client)
        self.assertEqual(client, self.repository.find_by_tax_id("test"))

    def test_save(self):
        client = ClientMother.normal_client(1)
        self.repository.conn = self.mock_conn_update()
        self.assertIsNone(self.repository.save(client))

    def test_get_id(self):
        client = ClientMother.normal_client(1)
        self.repository.conn = self.mock_conn_fetch_one(client.to_dict())
        self.assertEqual(client, self.repository.get_id(1))