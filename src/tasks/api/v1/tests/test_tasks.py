from typing import Callable
import pytest

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.response import Response

from accounts.models import User


TASKS_LIST_URL = reverse("task-list")


@pytest.mark.django_db
def test_create_task(api: APIClient, authorize: Callable[[APIClient, User], None], user: User) -> None:
    authorize(api, user)

    payload = {
        "title": "Test task title",
        "description": "Test task description",
    }
    response_create: Response = api.post(TASKS_LIST_URL, data=payload, format="json")
    print(response_create.data)
    assert response_create.status_code == 201
    assert set(response_create.data.keys()) == {
        "id",
        "title",
        "description",
        "created_at",
        "status",
    }


@pytest.mark.django_db
def test_list_tasks(api: APIClient, authorize: Callable[[APIClient, User], None], user: User) -> None:
    authorize(api, user)

    payload = {
        "title": "Test task title",
        "description": "Test task description",
    }
    response_create: Response = api.post(TASKS_LIST_URL, data=payload, format="json")
    assert response_create.status_code == 201
    assert set(response_create.data.keys()) == {
        "id",
        "title",
        "description",
        "created_at",
        "status",
    }

    response_list: Response = api.get(TASKS_LIST_URL)
    assert response_list.status_code == 200
    assert set(response_list.data.keys()) == {
        "count",
        "next",
        "previous",
        "results",
    }

