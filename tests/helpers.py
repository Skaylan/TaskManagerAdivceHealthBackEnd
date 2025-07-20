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

CREATE_CATEGORY_PAYLOAD = {
    'email': 'test@example.com',
    'name': 'categoria teste',
    'color': '#FFFFFF'
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

def update_task_status(client, task_id: int, status: bool):
    return client.put(f'{ENDPOINT}/update_task_status', {'task_id': task_id, 'status': status})

def update_task_infos(client, payload):
    return client.put(f'{ENDPOINT}/update_task_infos', payload, format='json')


def authenticate(client, email: str, password: str):
    return client.post(f'{ENDPOINT}/authenticate', {'email': email, 'password': password}, format='json')

def create_category(client, payload: dict):
    return client.post(f'{ENDPOINT}/create_category', payload, format='json')

def get_user_categories_by_email(client, email: str):
    return client.get(f'{ENDPOINT}/get_user_categories_by_email?email={email}')

def delete_category(client, category_id: int):
    return client.delete(f'{ENDPOINT}/delete_category', {'category_id': category_id})

def update_category(client, payload: dict):
    return client.put(f'{ENDPOINT}/update_category', payload, format='json')