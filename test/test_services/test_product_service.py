from unittest.mock import patch
import unittest
import random

from app.entities.enums.clientStatus import ClientStatus
from app.services.productService import  ProductService
from test.mothers.productMother import ProductMother


class TestProductService(unittest.TestCase):
    def setUp(self):
        self.mock_product_repository = patch('app.repositories.productRepository.ProductRepository').start()
        self.product_service = ProductService(self.mock_product_repository)

    def tearDown(self):
        patch.stopall()

    @patch('app.repositories.productRepository.ProductRepository.get_all')
    def test_get_all(self, mock_get_all):
        # Arrange
        mocked_product_a = ProductMother.normal_product(random.randint(1, 100))
        mocked_product_b = ProductMother.normal_product(random.randint(1, 100))
        mocked_product_list = [mocked_product_a, mocked_product_b]
        mock_get_all.return_value = mocked_product_list

        # Act
        result = self.product_service.get_all()

        # Assert
        mock_get_all.assert_called_once()
        self.assertEqual(result, mocked_product_list)
