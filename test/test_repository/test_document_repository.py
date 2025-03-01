import unittest
from unittest.mock import patch, MagicMock
from app.repositories.documentRepository import DocumentRepository
from app.entities.enums.status import Status

class DocumentRepositoryTestCase(unittest.TestCase):

    def test_get_all(self):

        mock_rows = [
            {
                "document_id": 1,
                "client_id": 1,
                "client_name": "John Doe",
                "client_status": Status.ACTIVE.get_value(),
                "amount": 100.0,
            },
            {
                "document_id": 2,
                "client_id": 2,
                "client_name": "Jane Smith",
                "client_status": Status.ACTIVE.get_value(),
                "amount": 200.0,
            },
        ]

        mock_response_dtos = [
            MagicMock(to_dict=lambda: {"id": 1, "client": "John Doe", "amount": 100.0}),
            MagicMock(to_dict=lambda: {"id": 2, "client": "Jane Smith", "amount": 200.0}),
        ]

        with patch("app.repositories.documentRepository.ResponseDocumentDtoFactory.from_list",
                   return_value=mock_response_dtos) as mock_factory:

            with patch("app.repositories.documentRepository.ConnectionManager") as mock_connection_manager, \
                    patch("app.repositories.documentRepository.CursorManager") as mock_cursor_manager:

                mock_cursor = MagicMock()
                mock_cursor.fetchall.return_value = mock_rows
                mock_cursor_manager.return_value.__enter__.return_value = mock_cursor

                repo = DocumentRepository(pool_connection="mock_pool")

                result = repo.get_all()

                expected_result = [
                    {"id": 1, "client": "John Doe", "amount": 100.0},
                    {"id": 2, "client": "Jane Smith", "amount": 200.0},
                ]
                assert result == expected_result

                mock_factory.assert_called_once_with(mock_rows)

                expected_sql = f"SELECT * FROM documents d inner join clients c on d.client_id = c.client_id WHERE  client_status = '{Status.ACTIVE.get_value()}'"
                mock_cursor.execute.assert_called_once_with(expected_sql)
