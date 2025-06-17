# 🚀 Lead Management Application

This is a Django-based web application designed for managing and tracking leads, featuring:

- ✅ Django REST Framework API
- 🐘 PostgreSQL as the database
- 🧵 Celery + Redis for asynchronous task handling
- 📩 Email notifications
- 🐳 Dockerized deployment
- 🌐 Nginx reverse proxy
- ☁️ Deployed to AWS EC2

---

## 🛠 Technologies Used

| Layer          | Technology         |
|----------------|--------------------|
| Backend        | Django, DRF        |
| Async Tasks    | Celery + Redis     |
| Database       | PostgreSQL         |
| Deployment     | Docker + EC2       |
| Reverse Proxy  | Nginx              |

---

## 📦 Project Structure

```bash
.
├── core/                    # Django project
├── lead/                    # App for managing leads
├── users/                   # User registration and auth
├── nginx/
│   └── default.conf         # Nginx config
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

🚀 Running Locally
Clone the repository
```bash
git clone https://github.com/Shohruxshoh/lead.git
cd lead
```
Create .env file
```bash
cp .env.example .env
```
Run with Docker
```bash
docker-compose up --build
```
    The app will be available at:
    📍 http://localhost — served by Nginx
    📍 http://localhost:8000 — Django directly
Create Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

🧪 Testing
```bash
docker-compose exec web pytest
```

📄 API Documentation
Swagger UI available at:
📍 http://localhost/api/docs/


👤 Author
Shohrux Nasriddinov
