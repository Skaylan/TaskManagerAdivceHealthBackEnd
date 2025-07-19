import pytest
from rest_framework.test import APIClient
from tests.helpers import *


client = APIClient()

@pytest.mark.django_db
def test_create_task():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201
    assert task_response.data['task']['title'] == ADD_TASK_PAYLOAD['title']
    assert task_response.data['message'] == 'Task successfully created!'

@pytest.mark.django_db
def get_tasks_by_user_email():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201

    get_task_response = get_tasks_by_user_email(client, CREATE_USER_PAYLOAD['email'])
    assert get_task_response.status_code == 200
    assert get_task_response.data['tasks'][0]['title'] == ADD_TASK_PAYLOAD['title']
    assert get_task_response.data['amount_of_tasks'] == 1

