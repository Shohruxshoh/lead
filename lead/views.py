# leads/views.py
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Lead
from .serializers import LeadSerializer, LeadUpdateSerializer
from .tasks import send_lead_emails
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

@extend_schema(
    request={
        'multipart/form-data': LeadSerializer
    },
    responses=LeadSerializer,
    description="Fayl bilan Lead yaratish (CV yuklanadi)",
)
class LeadCreateAPIView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_create(self, serializer):
        lead = serializer.save()
        full_name = f"{lead.first_name} {lead.last_name}"
        send_lead_emails.delay(lead.email, 'attorney@example.com', full_name)


class LeadListAPIView(generics.ListAPIView):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['email', 'first_name', 'last_name', 'state']

    filterset_fields = ['state']

    ordering_fields = ['created_at', 'first_name', 'last_name', 'email']

    def get_queryset(self):
        if not self.request.user.is_staff:
            raise PermissionDenied("Faqat adminlar uchun!")
        return super().get_queryset()


class LeadRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = LeadUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_staff:
            raise PermissionDenied("Faqat adminlar uchun!")
        return Lead.objects.all()
