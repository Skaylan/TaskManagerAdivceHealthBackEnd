import pytest
from rest_framework.test import APIClient
from tests.helpers import *


client = APIClient()

@pytest.mark.django_db
def test_authenticate():
    """
    Test the authenticate route.

    This test creates a user, then tries to authenticate with it.
    It checks that the returned user has the same email as the one created, and that the token is not empty.
    """
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    auth_response = authenticate(client, CREATE_USER_PAYLOAD['email'], CREATE_USER_PAYLOAD['password'])
    assert auth_response.status_code == 200
    assert auth_response.data['user']['email'] == CREATE_USER_PAYLOAD['email']
    assert auth_response.data['token'] != ''