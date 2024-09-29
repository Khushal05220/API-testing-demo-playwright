import requests

def test_get_user_content():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    user = response.json()
    assert user["id"] == 1
    assert "name" in user
    assert "username" in user

if __name__ == "__main__":
    test_get_user_content()