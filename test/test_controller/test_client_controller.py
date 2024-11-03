import json
import random
import unittest
from http import HTTPStatus

import app
from unittest.mock import patch

from app.entities.client import Client
from test.mothers.clientMother import ClientMother


class ClientControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app().test_client()

    @patch('app.services.clientService.ClientService.get_id')
    def test_get_id(self, mock_get_id):
        #Arrange
        id: int = 1
        mocked_client: Client = ClientMother.normal_client(id)
        expected_client: json = {'address': mocked_client.address,
             'city': mocked_client.city,
             'client_type': mocked_client.client_type.get_type(),
             'country': mocked_client.country,
             'email': mocked_client.email,
             'name': mocked_client.name,
             'phone': mocked_client.phone,
             'pk_client': str(id),
             'state': mocked_client.state,
             'status': mocked_client.status.ACTIVE.get_value(),
             'tax_condition': mocked_client.tax_condition.get_condition(),
             'tax_id': mocked_client.tax_id,
             'type_id': mocked_client.type_id.get_type()}

        mock_get_id.return_value = mocked_client

        #Act
        result = self.app.get('/clients/'+str(id))

        #Assert
        self.assertEqual(expected_client, result.json)
        self.assertEqual(HTTPStatus.OK.value, result.status_code)

    @patch('app.services.clientService.ClientService.get_all')
    def test_get_all(self, mock_get_all):
        #Arrange
        id_a: int = 1
        id_b: int = 2
        mocked_client_a: Client = ClientMother.normal_client(id_a)
        mocked_client_b: Client = ClientMother.normal_client(id_b)
        mocked_client_list:  list[Client] = [
            mocked_client_a,
            mocked_client_b,
        ]
        expected_list = [{
            'address': mocked_client_a.address,
            'city': mocked_client_a.city,
            'client_type': mocked_client_a.client_type.get_type(),
            'country': mocked_client_a.country,
            'email': mocked_client_a.email,
            'name': mocked_client_a.name,
            'phone': mocked_client_a.phone,
            'pk_client': str(id_a),
            'state': mocked_client_a.state,
            'status': mocked_client_a.status.ACTIVE.get_value(),
            'tax_condition': mocked_client_a.tax_condition.get_condition(),
            'tax_id': mocked_client_a.tax_id,
            'type_id': mocked_client_a.type_id.get_type()
            },{
            'address': mocked_client_b.address,
            'city': mocked_client_b.city,
            'client_type': mocked_client_b.client_type.get_type(),
            'country': mocked_client_b.country,
            'email': mocked_client_b.email,
            'name': mocked_client_b.name,
            'phone': mocked_client_b.phone,
            'pk_client': str(id_b),
            'state': mocked_client_b.state,
            'status': mocked_client_b.status.ACTIVE.get_value(),
            'tax_condition': mocked_client_b.tax_condition.get_condition(),
            'tax_id': mocked_client_b.tax_id,
            'type_id': mocked_client_b.type_id.get_type()
        }]
        mock_get_all.return_value = mocked_client_list

        #Act
        result = self.app.get('/clients/')

        #Assert
        self.assertEqual(expected_list, result.json)
        self.assertEqual(HTTPStatus.OK.value, result.status_code)

    @patch('app.services.clientService.ClientService.create')
    def test_create(self, mock_create):
        #Arrange
        mocked_client: Client = ClientMother.normal_client(random.randint(1, 100))
        client_data_req = {
            "name": mocked_client.name,
            "address": mocked_client.address,
            "city": mocked_client.city,
            "state": mocked_client.state,
            "country": mocked_client.country,
            "email": mocked_client.email,
            "phone": mocked_client.phone,
            "type_id": mocked_client.type_id.get_type(),
            "tax_id": mocked_client.tax_id,
            "tax_condition": mocked_client.tax_condition.get_condition(),
            "client_type": mocked_client.client_type.get_type()
        }

        mock_create.return_value = mocked_client.pk_client
        expected_response = {"client_id": mocked_client.pk_client}

        #Act
        result = self.app.post('/clients/', data=json.dumps(client_data_req), content_type='application/json')

        #Assert
        self.assertEqual(expected_response, result.get_json())
        self.assertEqual(HTTPStatus.CREATED.value, result.status_code)

    @patch('app.services.clientService.ClientService.modify')
    def test_modify(self, mock_modify):
        #Arrange
        mocked_client: Client = ClientMother.normal_client(random.randint(1, 100))
        client_data_req = {
            "name": mocked_client.name,
            "address": mocked_client.address,
            "city": mocked_client.city,
            "state": mocked_client.state,
            "country": mocked_client.country,
            "email": mocked_client.email,
            "phone": mocked_client.phone,
            "type_id": mocked_client.type_id.get_type(),
            "tax_id": mocked_client.tax_id,
            "tax_condition": mocked_client.tax_condition.get_condition(),
            "client_type": mocked_client.client_type.get_type()
        }
        expected_response = {"message": "Client modify successfully"}

        #Act
        result = self.app.put('/clients/1', data=json.dumps(client_data_req), content_type='application/json')

        #Assert
        self.assertEqual(expected_response, result.get_json())
        self.assertEqual(HTTPStatus.OK.value, result.status_code)


    @patch('app.services.clientService.ClientService.delete')
    def test_delete(self, mock_delete):
        #Arrange
        expected_response = {"message": "Client deleted successfully"}

        #Act
        result = self.app.delete('/clients/'+ str(random.randint(1, 100)))

        #Assert
        self.assertEqual(expected_response, result.get_json())
        self.assertEqual(HTTPStatus.OK.value, result.status_code)
