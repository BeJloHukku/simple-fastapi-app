import requests
import sys
import os


def add(name: str, email: str):
    if os.getenv('RUNNING_IN_DOCKER'):
        base_url = "http://fastapi:8000"
    else:
        base_url = "http://localhost"
    
    json_data = {"name": name, "email": email}
    try:
        response = requests.post(url=f"{base_url}/users", json=json_data)
        print(response.text)
    except requests.RequestException as e:
        print(str(e))

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print(f"Некорректный ввод: {args}")
        exit(1)
    name, email = args
    add(name, email) 