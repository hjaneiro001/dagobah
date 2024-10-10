from unittest.mock import Mock

import pytest

from app.services.clientService import ClientService


@pytest.fixture
def mock_client_repository():
    return Mock()  # Este fixture crea un mock del repositorio

@pytest.fixture
def client_service(mock_client_repository):
    return ClientService(mock_client_repository)

def test_sum():
    assert True