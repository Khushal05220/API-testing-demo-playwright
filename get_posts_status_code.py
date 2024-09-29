import requests

def test_get_posts_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

if __name__ == "__main__":
    test_get_posts_status_code()