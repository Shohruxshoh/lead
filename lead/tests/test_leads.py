# -*- coding: utf-8 -*-
import pytest
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from lead.models import Lead


@pytest.mark.django_db
def test_create_lead():
    client = APIClient()
    resume_file = SimpleUploadedFile(
        name="cv.pdf",
        content=b"%PDF-1.4\nThis is a fake PDF file for testing\n",
        content_type="application/pdf"
    )

    payload = {
        "first_name": "Ali",
        "last_name": "Valiyev",
        "email": "ali@example.com",
        "resume": resume_file
    }

    response = client.post("/api/leads/create/", payload, format='multipart')
    assert response.status_code == 201
    assert Lead.objects.count() == 1


@pytest.mark.django_db
def test_lead_list_for_admin():
    client = APIClient()
    admin = User.objects.create_user(username="admin", password="admin123", is_staff=True)
    client.force_authenticate(user=admin)

    resume_file = SimpleUploadedFile(
        name="cv.pdf",
        content=b"%PDF-1.4\nfake content\n",
        content_type="application/pdf"
    )

    Lead.objects.create(
        first_name="Ali",
        last_name="Valiyev",
        email="ali@example.com",
        resume=resume_file
    )

    response = client.get("/api/leads/")
    assert response.status_code == 200
    assert "results" in response.data
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_lead_state_update():
    client = APIClient()
    admin = User.objects.create_user(username="admin", password="admin123", is_staff=True)
    client.force_authenticate(user=admin)

    resume_file = SimpleUploadedFile(
        name="cv.pdf",
        content=b"%PDF-1.4\nupdate content\n",
        content_type="application/pdf"
    )

    lead = Lead.objects.create(
        first_name="Ali",
        last_name="Valiyev",
        email="ali@example.com",
        resume=resume_file
    )

    response = client.patch(f"/api/leads/{lead.id}/", {"state": "REACHED_OUT"})
    assert response.status_code == 200

    lead.refresh_from_db()
    assert lead.state == "REACHED_OUT"
