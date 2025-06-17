from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from .serializers import CustomLoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



@extend_schema(
    request=CustomLoginSerializer,
    responses={
        200: OpenApiExample(
            name="Login successful",
            value={
                "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
                "access": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
                "user": {
                    "id": 1,
                    "username": "admin",
                    "email": "admin@example.com"
                }
            },
            response_only=True,
        ),
        400: OpenApiExample(
            name="Login error",
            value={"non_field_errors": ["Login yoki parol noto‘g‘ri."]},
            response_only=True,
        ),
    },
    tags=["Auth"],
    description="Foydalanuvchi username va password bilan tizimga kiradi. JWT token qaytariladi.",
)
class CustomLoginView(APIView):
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
