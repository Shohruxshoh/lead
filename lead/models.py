from django.db import models

# Create your models here.
# leads/models.py
from django.db import models

class Lead(models.Model):
    STATE_CHOICES = [
        ('PENDING', 'Pending'),
        ('REACHED_OUT', 'Reached Out'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
