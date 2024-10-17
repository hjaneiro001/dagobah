import json
import random
import unittest
from http import HTTPStatus
from itertools import product

import app
from unittest.mock import patch

from app.entities.product import Product
from test.mothers.productMother import ProductMother


class ProductControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app().test_client()

    @patch('app.services.productService.ProductService.get_all')
    def test_get_all(self, mock_get_all):
        # Arrange
        product_id_a: int = 1
        product_id_b: int = 2
        mocked_product_a: Product = ProductMother.normal_product(product_id_a)
        mocked_product_b: Product = ProductMother.normal_product(product_id_b)
        mocked_product_list: list[Product] = [
            mocked_product_a,
            mocked_product_b,
        ]
        expected_list = [{
            'code': mocked_product_a.code,
            'bar_code': mocked_product_a.bar_code,
            'name': mocked_product_a.name,
            'description': mocked_product_a.description,
            'pack': mocked_product_a.pack,
            'price': mocked_product_a.price,
            'currency': mocked_product_a.currency.value,
            'iva': mocked_product_a.iva.value,
            'product_type': mocked_product_a.product_type.value,
            'status': mocked_product_a.status.value,
            'product_id': 1,
        }, {
            'code': mocked_product_b.code,
            'bar_code': mocked_product_b.bar_code,
            'name': mocked_product_b.name,
            'description': mocked_product_b.description,
            'pack': mocked_product_b.pack,
            'price': mocked_product_b.price,
            'currency': mocked_product_b.currency.value,
            'iva': mocked_product_b.iva.value,
            'product_type': mocked_product_b.product_type.value,
            'status': mocked_product_b.status.value,
           'product_id': 2,
        }]
        mock_get_all.return_value = mocked_product_list

        # Act
        result = self.app.get('/products/')

        # Assert
        self.assertEqual(expected_list, result.json)
        self.assertEqual(HTTPStatus.OK.value, result.status_code)


    @patch('app.services.productService.ProductService.get_id')
    def test_get_id(self, mock_get_id):

         id: int = 1
         mocked_product: Product = ProductMother.normal_product(id)
         expected_product: json = {
            'code': mocked_product.code,
            'bar_code': mocked_product.bar_code,
            'name': mocked_product.name,
            'description': mocked_product.description,
            'pack': mocked_product.pack,
            'price': mocked_product.price,
            'currency': mocked_product.currency.value,
            'iva': mocked_product.iva.value,
            'product_type': mocked_product.product_type.value,
            'status': mocked_product.status.value,
            'product_id': id,
        }

         mock_get_id.return_value = mocked_product

         #Act
         result = self.app.get('/products/'+str(id))

         #Assert
         self.assertEqual(expected_product, result.json)
         self.assertEqual(HTTPStatus.OK.value, result.status_code)


    @patch('app.services.productService.ProductService.create')
    def test_create(self, mock_create):
        # Arrange
        mocked_product :Product = ProductMother.normal_product(random.randint(1, 100))
        product_data_req = {
            'code': mocked_product.code,
            'bar_code': mocked_product.bar_code,
            'name': mocked_product.name,
            'description': mocked_product.description,
            'pack': mocked_product.pack,
            'price': mocked_product.price,
            'currency': mocked_product.currency.value,
            'iva': mocked_product.iva.value,
            'product_type': mocked_product.product_type.value
        }

        mock_create.return_value = mocked_product.product_id
        expected_response = {"product_id": mocked_product.product_id}

        # Act
        result = self.app.post('/products/', data=json.dumps(product_data_req), content_type='application/json')

        # Assert
        self.assertEqual(expected_response, result.get_json())
        self.assertEqual(HTTPStatus.CREATED.value, result.status_code)

    @patch('app.services.productService.ProductService.modify')
    def test_modify(self, mock_modify):
        mocked_product: Product = ProductMother.normal_product(random.randint(1, 100))
        product_data_req = {
            'code': mocked_product.code,
            'bar_code': mocked_product.bar_code,
            'name': mocked_product.name,
            'description': mocked_product.description,
            'pack': mocked_product.pack,
            'price': mocked_product.price,
            'currency': mocked_product.currency.value,
            'iva': mocked_product.iva.value,
            'product_type': mocked_product.product_type.value
        }

        expected_response = {"message": "Product modify successfully"}

         # Act
        result = self.app.put('/products/' + str(random.randint(1, 100)), data=json.dumps(product_data_req), content_type='application/json')

        # Assert
        self.assertEqual(expected_response, result.get_json())
        self.assertEqual(HTTPStatus.OK.value, result.status_code)


    @patch('app.services.productService.ProductService.delete')
    def test_delete(self, mock_delete):
        # Arrange
        expected_response = {"message": "Product deleted successfully"}

        # Act
        result = self.app.delete('/products/' + str(random.randint(1, 100)))

        # Assert
        self.assertEqual(expected_response, result.get_json())
        self.assertEqual(HTTPStatus.OK.value, result.status_code)

