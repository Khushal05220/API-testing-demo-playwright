import requests

def test_get_users_response_headers():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

if __name__ == "__main__":
    test_get_users_response_headers()