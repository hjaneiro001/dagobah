from unittest.mock import patch
import unittest
import random

from app.entities.enums.clientStatus import ClientStatus
from app.entities.product import Product
from app.exceptions.productAlreadyExistException import ProductAlreadyExistsException
from app.exceptions.productNotFoundException import ProductNotFoundException
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


    @patch('app.repositories.productRepository.ProductRepository.get_id')
    def test_get_id_success(self, mock_get_id):
        # Arrange
        mocked_product = ProductMother.normal_product(random.randint(1, 100))
        mock_get_id.return_value = mocked_product
        # Act
        result = self.product_service.get_id(mocked_product.product_id)
        # Assert
        mock_get_id.assert_called_once_with(mocked_product.product_id)
        self.assertEqual(result, mocked_product)

    @patch('app.repositories.productRepository.ProductRepository.get_id')
    def test_get_id_not_found(self, mock_get_id):
        # Arrange
        mock_get_id.return_value = None

        # Act & Assert
        with self.assertRaises(ProductNotFoundException):
            self.product_service.get_id(1)


    @patch('app.repositories.productRepository.ProductRepository.create')
    @patch('app.repositories.productRepository.ProductRepository.find_by_code')
    def test_create_product_success(self, mock_find_by_code, mock_create):
        # Arrange
        mocked_product = ProductMother.normal_product(random.randint(1, 100))
        mock_find_by_code.return_value = None
        mock_create.return_value = mocked_product.product_id

        # Act
        product_id = self.product_service.create(mocked_product)

        # Assert
        mock_find_by_code.assert_called_once_with(mocked_product.code)
        mock_create.assert_called_once_with(mocked_product)
        self.assertEqual(product_id, mocked_product.product_id)
        self.assertEqual(mocked_product.status, ClientStatus.ACTIVE)


    @patch('app.repositories.productRepository.ProductRepository.create')
    @patch('app.repositories.productRepository.ProductRepository.find_by_code')
    def test_create_product_already_exists(self, mock_find_by_code, mock_create):
        # Arrange
        mocked_product = ProductMother.normal_product(random.randint(1, 100))
        mock_find_by_code.return_value = mocked_product

        # Act & Assert
        with self.assertRaises(ProductAlreadyExistsException):
            self.product_service.create(mocked_product)
        mock_create.assert_not_called()


