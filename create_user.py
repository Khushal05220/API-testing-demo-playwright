import requests

def test_create_user():
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)
    assert response.status_code == 201
    assert response.json()["name"] == new_user["name"]

if __name__ == "__main__":
    test_create_user()