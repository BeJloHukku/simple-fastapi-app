import requests
import sys


def add(name: str, email: str):
    json_data = {"name": name, "email": email}
    try:
        response = requests.post(url="http://localhost/users" ,json=json_data)
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