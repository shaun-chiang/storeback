# Storeback
Demo for a simple CRUD Flask backend for a store, companion backend for [Storefront](https://github.com/shaun-chiang/storefront)

## Setup
Activate venv:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start mongodb and set env var:
```
export MONGO_URL=mongodb://0.0.0.0:27017/
docker-compose up
```

Run application at `localhost:5000`:
```
cd app
flask run
```

## Endpoints
- READ list of all items in the store
```
GET /items
Description: Returns list of items.
Responses:
200 OK
[
  {
    "_id": "5f758ccf94b1177406b80fdd",
    "name": "Milk Carton",
    "price": 2.55
  }
]
```
- CREATE an item in the store
```
POST /items
Description: Creates an item as specified in body.
Headers:
"content-type": "application/json"
Body:
{
  "name": "Milk Case",
  "price": 25.50
}
Responses:
200 OK
{
  "_id": "5f759a412a0ade1c0d1c4ea9",
  "name": "Milk Case",
  "price": 25.5
}
422 Unprocessable Entity
{
  "error": "{'price': ['Not a valid number.']}"
}
```
- UPDATE an item in the store
```
PUT /items/<id>
Description: Updates item at specified id.
Headers:
"content-type": "application/json"
Body:
{
  "name": "UHT Milk Case",
  "price": 26.5
}
Responses:
200 OK
{
  "name": "UHT Milk Case",
  "price": 26.5
}
404 Not Found
{
  "error": "item not found"
}
422 Unprocessable Entity
{
  "error": "{'price': ['Not a valid number.']}"
}
```
- DELETE an item in the store
```
DELETE /items/<id>
Description: Deletes item at specified id.
Responses:
204 No Content
404 Not Found
{
  "error": "item not found"
}
```
- Responses are all in JSON.
