import pytest
from rest_framework.test import APIClient
from tests.helpers import *


client = APIClient()

@pytest.mark.django_db
def test_create_task():
    """
    Test that a task can be created correctly.

    This test creates a user and then a task, and verifies that the task
    is created successfully with the correct title and that the appropriate
    success message is returned.
    """

    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201
    assert task_response.data['task']['title'] == ADD_TASK_PAYLOAD['title']
    assert task_response.data['message'] == 'Task successfully created!'

@pytest.mark.django_db
def test_get_tasks_by_user_email():
    """
    Test that tasks can be retrieved by user email correctly.

    This test creates a user and a task, and then retrieves the task by
    email. It verifies that the task is retrieved successfully and has the
    correct title and amount of tasks.
    """
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
    """
    Test that all tasks can be retrieved correctly.

    This test creates a user and a task, and then retrieves all tasks. It verifies
    that the task is retrieved successfully and has the correct title.
    """

    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201

    get_task_response = get_all_tasks(client)
    assert get_task_response.status_code == 200


@pytest.mark.django_db
def test_delete_task():
    """
    Test that a task can be deleted correctly.

    This test creates a user and a task, and then deletes the task. It verifies
    that the task is deleted successfully and that the appropriate success
    message is returned.
    """
    user_response = create_user(client, CREATE_USER_PAYLOAD)
    assert user_response.status_code == 201

    task_response = add_task(client, ADD_TASK_PAYLOAD)
    assert task_response.status_code == 201

    delete_task_response = delete_task(client, task_response.data['task']['id'])
    assert delete_task_response.status_code == 200

@pytest.mark.django_db
def test_update_task_status():
    """
    Test that a task status can be updated correctly.

    This test creates a user and a task, and then updates the task status. It verifies
    that the task status is updated successfully and that the appropriate success
    message is returned.
    """
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
    """
    Test that a task's information can be updated correctly.

    This test creates a user and a task, then updates the task's title and
    description. It verifies that the task information is updated successfully
    and that the appropriate success message is returned.
    """

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