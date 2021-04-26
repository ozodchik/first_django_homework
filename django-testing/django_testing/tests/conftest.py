import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def course_fabric():
    def create(**kwargs):
        return baker.make("students.Course", **kwargs)
    return create


@pytest.fixture
def students_fabric():
    def create(**kwargs):
        return baker.make("students.Student", **kwargs)
    return create
