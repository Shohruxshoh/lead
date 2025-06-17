# users/tests/test_auth.py
# -*- coding: utf-8 -*-
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    response = client.post("/api/auth/register/", {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 201
    assert User.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    User.objects.create_user(username="admin", email="admin@example.com", password="admin123")
    response = client.post("/api/auth/login/", {
        "username": "admin",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
