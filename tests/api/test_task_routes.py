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
def test_get_tasks_by_user_email():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201

    get_task_response = get_tasks_by_user_email(client, CREATE_USER_PAYLOAD['email'])
    assert get_task_response.status_code == 200
    assert get_task_response.data['tasks'][0]['title'] == ADD_TASK_PAYLOAD['title']
    assert get_task_response.data['amount_of_tasks'] == 1


@pytest.mark.django_db
def test_get_all_tasks():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201

    get_task_response = get_all_tasks(client)
    assert get_task_response.status_code == 200


@pytest.mark.django_db
def test_delete_task():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201

    delete_task_response = delete_task(client, task_response.data['task']['id'])
    assert delete_task_response.status_code == 200

@pytest.mark.django_db
def test_update_task_status():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.data['task']['is_done'] == False
    assert task_response.status_code == 201

    update_task_response = update_task_status(client, task_response.data['task']['id'], True)
    assert update_task_response.status_code == 200
    assert task_response.data['task']['is_done'] == False


@pytest.mark.django_db
def test_update_task_infos():
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201
    assert task_response.data['task']['title'] == ADD_TASK_PAYLOAD['title']

    payload = {
        "title": "Tarefa atualizada",
        "description": "Descrição da tarefa atualizada",
        'task_id': task_response.data['task']['id'],
        'category_id': ''
    }

    update_task_response = update_task_infos(client, payload)
    assert update_task_response.status_code == 200
    assert update_task_response.data['message'] == 'Task successfully updated!'
    assert update_task_response.data['task']['title'] == "Tarefa atualizada"
    assert update_task_response.data['task']['description'] == "Descrição da tarefa atualizada"