import unittest
from http import HTTPStatus

import app
from unittest.mock import patch

from app.entities.client import Client
from app.entities.enums.clientStatus import ClientStatus
from app.entities.enums.clientType import ClientType
from app.entities.enums.taxCondition import TaxCondition
from app.entities.enums.typeId import TypeId


class ClientControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app().test_client()

    @patch('app.services.clientService.ClientService.get_id')
    def test_get_id(self, mock_get_id):
        mock_get_id.return_value = Client(1,'test','test','test','test','test',
                                          'test','test',TypeId.CUIT,'test',
                                          TaxCondition.RI,ClientType.C,ClientStatus.ACTIVE)
        result = self.app.get('/clients/1')
        self.assertEqual(
            {'address': 'test', 'city': 'test', 'client_type': 'CLIENTE', 'country': 'test', 'email': 'test',
             'name': 'test', 'phone': 'test', 'pk_client': '1', 'state': 'test', 'status': 'ACTIVE',
             'tax_condition': 'RESPONSABLE INSCRIPTO', 'tax_id': 'test', 'type_id': 'CUIT'}, result.json)
        self.assertEqual(HTTPStatus.OK.value, result.status_code)

