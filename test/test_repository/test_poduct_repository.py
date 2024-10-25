import unittest
from unittest.mock import MagicMock

from app.entities.enums.status import Status
from app.entities.product import Product
from app.repositories.productRepository import ProductRepository
from test.mothers.productMother import ProductMother
from unittest.mock import ANY

class ProductRepositoryTestCase(unittest.TestCase):

    def test_get_all(self):
        #Arrange
        expected_sentence: str = "SELECT * FROM Products WHERE product_status = 'ACTIVE'"
        expected_product: Product = ProductMother.normal_product(1)
        expected_db_response = [
            {
                'product_id': expected_product.product_id,
                'product_code': expected_product.code,
                'product_bar_code': expected_product.bar_code,
                'product_name': expected_product.name,
                'product_description': expected_product.description,
                'product_pack': expected_product.pack,
                'product_price': expected_product.price,
                'product_currency': expected_product.currency.value,
                'product_iva': expected_product.iva.value,
                'product_type': expected_product.product_type.value,
                'product_status': expected_product.status.get_status()
            }
        ]

        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = expected_db_response

        product_repository = ProductRepository(mock_connection)

        #Act
        products = product_repository.get_all()

        #Assert
        assert len(products) == 1
        assert products[0] == expected_product
        mock_cursor.execute.assert_called_with(expected_sentence)

    def test_get_id(self):
        # Arrange
        expected_product: Product = ProductMother.normal_product(1)
        expected_sentence: str = "SELECT * FROM products WHERE product_id = %s AND product_status = 'ACTIVE'"
        expected_db_response = {
                    'product_id': expected_product.product_id,
                    'product_code': expected_product.code,
                    'product_bar_code': expected_product.bar_code,
                    'product_name': expected_product.name,
                    'product_description': expected_product.description,
                    'product_pack': expected_product.pack,
                    'product_price': expected_product.price,
                    'product_currency': expected_product.currency.value,
                    'product_iva': expected_product.iva.value,
                    'product_type': expected_product.product_type.value,
                    'product_status': expected_product.status.get_status()
                }

        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = expected_db_response

        product_repository = ProductRepository(mock_connection)

        # Act
        products = product_repository.get_id(expected_product.product_id)

        # Assert
        assert products == expected_product
        mock_cursor.execute.assert_called_with(expected_sentence, (expected_product.product_id,))

    def test_create_success(self):
        # Arrange
        expected_product_id = 1
        product_to_create = ProductMother.normal_product(expected_product_id)
        expected_sql = """
                INSERT INTO products (product_code, product_bar_code, product_name, product_description, product_pack, product_price, product_currency, product_iva, product_type, product_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        expected_values = (
            product_to_create.code, product_to_create.bar_code, product_to_create.name, product_to_create.description,
            product_to_create.pack,
            product_to_create.price, product_to_create.currency.value, product_to_create.iva.value,
            product_to_create.product_type.value, product_to_create.status.get_status()
        )

        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.lastrowid = expected_product_id
        product_repository = ProductRepository(mock_connection)

        # Act
        actual = product_repository.create(product_to_create)

        #Assert
        assert actual == expected_product_id
        mock_cursor.execute.assert_called_with(ANY, expected_values)

    def test_save_success(self):
        product_to_modify = ProductMother.normal_product(1)

        expected_values = (
            product_to_modify.code, product_to_modify.name, product_to_modify.description, product_to_modify.bar_code,
            product_to_modify.pack, product_to_modify.price, product_to_modify.currency.value,
            product_to_modify.iva.value, product_to_modify.product_type.value, product_to_modify.status.get_status(),
            product_to_modify.product_id
        )

        # Mock objects
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        product_repository = ProductRepository(mock_connection)

        # Act
        product_repository.save(product_to_modify)

        # Assert
        mock_cursor.execute.assert_called_with(ANY, expected_values)
