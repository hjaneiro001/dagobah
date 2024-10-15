import json
import random
import unittest
from http import HTTPStatus

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
