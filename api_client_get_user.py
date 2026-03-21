from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()

# Используем метод create_user
create_user_response = users_gateway_client.create_user()
print('Create locust data:', create_user_response)

# Используем метод get_user
get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get locust data:', get_user_response)

