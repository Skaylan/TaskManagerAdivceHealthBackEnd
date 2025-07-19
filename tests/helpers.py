ENDPOINT = 'http://localhost:8000/api/v1'


CREATE_USER_PAYLOAD = {
    'name': 'Test User',
    'email': 'test@example.com',
    'password': 'password123',
    're_password': 'password123'
}

ADD_TASK_PAYLOAD = {
    'title': 'Tarefa 1',
    'description': 'Descrição da tarefa 1',
    'user_id': 1
}

def create_user(client, payload: dict):
    return client.post(f'{ENDPOINT}/create_user', payload, format='json')

def get_all_users(client):
    return client.get(f'{ENDPOINT}/get_all_users')

def get_user_by_email(client, email: str):
    return client.get(f'{ENDPOINT}/get_user_by_email?email={email}')

def add_task(client, payload: dict):
    return client.post(f'{ENDPOINT}/add_task', payload, format='json')

def get_tasks_by_user_email(client, email: int):
    return client.get(f'{ENDPOINT}/get_tasks_by_user_email?email={email}')

def get_all_tasks(client):
    return client.get(f'{ENDPOINT}/get_all_tasks')

def delete_task(client, task_id: int):
    return client.delete(f'{ENDPOINT}/delete_task', {'task_id': task_id})