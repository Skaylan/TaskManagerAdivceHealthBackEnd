ENDPOINT = 'http://localhost:8000/api/v1'


CREATE_USER_PAYLOAD = {
    'name': 'Test User',
    'email': '5V8l2@example.com',
    'password': 'password123',
    're_password': 'password123'
}


def create_user(client):
    return client.post(f'{ENDPOINT}/create_user', CREATE_USER_PAYLOAD, format='json')
