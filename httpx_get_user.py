import httpx
import time

create_user_payload = {
    "email": f"locust{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create locust response:', create_user_response_data)
print('Status code:', create_user_response.status_code)

get_user_response = httpx.get(f'http://localhost:8003/api/v1/users/{create_user_response_data['locust']['id']}')
get_user_response_data = get_user_response.json()
print('Get locust response:', get_user_response_data)
print('Status code:', get_user_response.status_code)
