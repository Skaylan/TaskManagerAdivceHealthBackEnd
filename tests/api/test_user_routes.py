import pytest
from rest_framework.test import APIClient
from tests.helpers import *

client = APIClient()

@pytest.mark.django_db
def test_create_user():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201


@pytest.mark.django_db
def test_get_all_users():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    user_response = get_all_users(client)
    assert user_response.status_code == 200
    assert user_response.data[0]['email'] == CREATE_USER_PAYLOAD['email']


@pytest.mark.django_db
def test_get_user_by_email():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    user_response = get_user_by_email(client, CREATE_USER_PAYLOAD['email'])
    assert user_response.status_code == 200
    assert user_response.data['email'] == CREATE_USER_PAYLOAD['email']