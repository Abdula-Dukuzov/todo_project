import os
import requests


API_URL = os.getenv("API_URL", "http://host.docker.internal:8000/")
# API_URL = os.getenv("API_URL", "http://localhost:8000/")
API_TOKEN = os.getenv("API_TOKEN")


def get_tasks(token):
    print(f"Пытаюсь подключиться к: {API_URL}api/tasks/ с токеном {token}")
    try:
        response = requests.get(
            f"{API_URL}api/tasks/",
            headers={"Authorization": f"Token {token}"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        if isinstance(data, list):
            return data
        return []
    except requests.exceptions.HTTPError as e:
        print("HTTPError:", e, e.response.text)
        return []
    except requests.exceptions.RequestException as e:
        print("RequestException:", e)
        return []


def create_task(token: str, data: dict):
    response = requests.post(
        f"{API_URL}api/tasks/",
        json=data,
        headers={
            "Authorization": f"Token {token}"
        },
        timeout=10
    )
    response.raise_for_status()
    return response.json()
