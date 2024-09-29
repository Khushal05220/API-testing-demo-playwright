import requests

def test_partial_update_user():
    updated_user = {
        "email": "john.doe.updated@example.com"
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/users/1", json=updated_user)
    assert response.status_code == 200
    assert response.json()["email"] == updated_user["email"]

if __name__ == "__main__":
    test_partial_update_user()