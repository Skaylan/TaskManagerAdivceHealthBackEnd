import pytest
from rest_framework.test import APIClient
from tests.helpers import *

client = APIClient()


@pytest.mark.django_db
def test_create_category():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    category_response = create_category(client, CREATE_CATEGORY_PAYLOAD)
    assert category_response.status_code == 201
    assert category_response.data['message'] == 'Category successfully created!'
    assert category_response.data['category']['name'] == CREATE_CATEGORY_PAYLOAD['name']
    assert category_response.data['category']['color'] == CREATE_CATEGORY_PAYLOAD['color']



@pytest.mark.django_db
def test_get_user_categories_by_email():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    category_response = create_category(client, CREATE_CATEGORY_PAYLOAD)
    assert category_response.status_code == 201

    get_category_response = get_user_categories_by_email(client, CREATE_USER_PAYLOAD['email'])
    assert get_category_response.status_code == 200
    assert get_category_response.data[0]['name'] == CREATE_CATEGORY_PAYLOAD['name']
    assert get_category_response.data[0]['color'] == CREATE_CATEGORY_PAYLOAD['color']


@pytest.mark.django_db
def test_delete_category():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    category_response = create_category(client, CREATE_CATEGORY_PAYLOAD)
    assert category_response.status_code == 201

    get_category_response = delete_category(client, category_response.data['category']['id'])
    assert get_category_response.status_code == 200
    assert get_category_response.data['message'] == 'Category successfully deleted!'

@pytest.mark.django_db
def test_update_category():
    update_payload = {
        "category_id": 1,
        "name": "new name",
        "color": "#000000"
    }

    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    category_response = create_category(client, CREATE_CATEGORY_PAYLOAD)
    assert category_response.status_code == 201

    update_category_response = update_category(client, update_payload)
    assert update_category_response.status_code == 200
    assert update_category_response.data['message'] == 'Category successfully updated!'
    assert update_category_response.data['category']['name'] == update_payload['name']
    assert update_category_response.data['category']['color'] == update_payload['color']