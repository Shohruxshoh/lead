from django.urls import path
from .views import LeadCreateAPIView, LeadListAPIView, LeadRetrieveUpdateAPIView

urlpatterns = [
    path('create/', LeadCreateAPIView.as_view(), name='lead-create'),
    path('', LeadListAPIView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadRetrieveUpdateAPIView.as_view(), name='lead-detail'),
]
