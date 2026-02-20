from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    # This built-in view handles token retrieval out of the box
    pass

class ProfileView(generics.RetrieveUpdateAPIView):
    # This satisfies the requirement for user profile management
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user