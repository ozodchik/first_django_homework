import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_course(api_client, course_fabric):
    # arrange
    course = course_fabric()
    url = reverse("courses-detail", args=(course.id, ))

    # act
    response = api_client.get(url)
    res_json = response.json()
    # assert
    assert res_json["id"] == course.id


@pytest.mark.django_db
def test_list_course(api_client, course_fabric):

    # arrange
    url = reverse("courses-list")
    quantity = 5
    course = course_fabric(_quantity=quantity)

#     act
    response = api_client.get(url)
    res_json = response.json()

#     assert
    assert quantity == len(res_json)


@pytest.mark.django_db
def test_course_filter(api_client, course_fabric):

    # arrange
    url = reverse("courses-list")
    quantity = 5
    course = course_fabric(_quantity=quantity)
    course_id = 4

    # act
    response = api_client.get(url, data={"id": course_id})

    # assert
    assert response.data[0]["id"] == course_id


@pytest.mark.django_db
def test_course_name_filter(api_client, course_fabric):

    # arrange
    url = reverse("courses-list")
    course1 = course_fabric(name="first")
    course2 = course_fabric(name="second")
    course_name = "first"

    # act
    response = api_client.get(url, data={"name": course_name})

    # assert
    assert response.data[0]["name"] == course_name


@pytest.mark.django_db
def test_create_course(api_client, course_fabric):

    # arrange
    url = reverse("courses-list")
    application_json = {
        "name": "my_course"
    }

    # act
    response = api_client.post(url, data=application_json)

    # assert
    assert response.status_code == 201


@pytest.mark.django_db
def test_patch_course(api_client, course_fabric):
    # arrange
    name = "my_course"
    application_json = {
        "name": name
    }
    course = course_fabric()
    url = reverse("courses-detail", args=(course.id, ))

    # act
    response = api_client.patch(url, data=application_json)

    # assert
    # 1 способ проверки assert response.data["name"] == name
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(api_client, course_fabric):

    # arrange
    course = course_fabric()
    url = reverse("courses-detail", args=(course.id, ))

    # act
    response = api_client.delete(url)

    # assert
    assert response.status_code == 204
