import httpx

# get
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

# post

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())

# headers

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.json())

# params

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json())

# file

files = {"file": ("example.txt", open("httpx.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())

# client

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

# client headers

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())
client.close()

# error

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# timeout

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")



