import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)        # 200
print(type(response.json()))            # Python list/dict

users = response.json()
for user in users:
    print(user["name"])            # Print each user's name
print(response.headers)            # Response headers
print(response.elapsed.total_seconds())  # Time taken for the request