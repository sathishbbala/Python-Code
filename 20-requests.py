import requests

response = requests.get(url = "https://api.restful-api.dev/objects/7")
data =  response.json()
print(type(data))

payload = {
    "name": "My Laptop",
    "data": {
        "brand": "Dell",
        "cpu": "i7",
        "ram": "16GB"
    }
}

r=requests.post("https://api.restful-api.dev/objects",json=payload)
print(r.json())