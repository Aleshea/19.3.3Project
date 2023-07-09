import requests
import json

#GET
status = 'available'
res = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params={'status': status},
                   headers={'accept': 'application/json'})
print("Status:", res.status_code)
print("Data:", res.json())


#POST
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Nikolay",
  "photoUrls": [
    "photo.jpg"
  ],
  "tags": [
    {
      "id": 0,
      "name": "kitty"
    }
  ],
  "status": "available"
}
res_post = requests.post(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(new_pet))
print("Status:", res_post.status_code)
print("Data:", res.json())


#PUT
data = {
  "id": 100890,
  "category": {
    "id": 1,
    "name": "cat"
  },
  "name": "Kuzko",
  "photoUrls": [
    "photo.jpg"
  ],
  "tags": [
    {
      "id": 1,
      "name": "cat"
    }
  ],
  "status": "available"
}
res_put = requests.put(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(data))
print("Status:", res_put.status_code)
print("Data:", res.json())


#DELETE
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{id}", headers={'accept': 'application/json'})
print("Status:", res_put.status_code)
print("Data:", res.json())