import pytest
from rest_framework.test import APIClient
from tests.helpers import *


client = APIClient()


@pytest.mark.django_db
def test_create_user():
    user_response = create_user(client)
    assert user_response.status_code == 201