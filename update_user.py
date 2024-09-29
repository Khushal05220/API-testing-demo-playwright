import requests

def test_update_user():
    updated_user = {
        "name": "John Doe Updated",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=updated_user)
    assert response.status_code == 200
    assert response.json()["name"] == updated_user["name"]

if __name__ == "__main__":
    test_update_user()