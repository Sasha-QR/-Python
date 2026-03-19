import requests
import uuid

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "В личном письме наставнику"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}



# Вспомогательная функция

def create_project():
    url = f"{BASE_URL}/projects"
    payload = {
        "title": f"Test Project {uuid.uuid4()}",
        "users": {}
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201
    return response.json()["id"]



# POST /projects


def test_create_project_positive():
    url = f"{BASE_URL}/projects"
    payload = {
        "title": f"Project {uuid.uuid4()}",
        "users": {}
    }

    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_no_title():
    url = f"{BASE_URL}/projects"
    payload = {
        "users": {}
    }

    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code in [400, 422]



# PUT /projects/{id}

def test_update_project_positive():
    project_id = create_project()

    url = f"{BASE_URL}/projects/{project_id}"
    payload = {
        "title": "Updated Project Name"
    }

    response = requests.put(url, json=payload, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_update_project_negative_wrong_id():
    url = f"{BASE_URL}/projects/invalid-id"
    payload = {
        "title": "Should Fail"
    }

    response = requests.put(url, json=payload, headers=HEADERS)

    assert response.status_code == 404



# GET /projects/{id}


def test_get_project_positive():
    project_id = create_project()

    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_not_found():
    url = f"{BASE_URL}/projects/invalid-id"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 404