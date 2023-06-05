from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnowLogoutAllView
)
from user.models import User
from .serializers import RegisterUserSerializer, UserSerializer

# Create your views here.

class RegisterUserAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        user = serializer.save()
        request.user = user
        # once user got created, create token for user.
        return super(RegisterUserAPI, self).post(request, format=None)
        


class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed(detail="Invalid credentials")
        
        request.user = user

        return super(LoginAPI, self).post(request, format=None)


class LogoutAPI(KnoxLogoutView):
    def post(self, request):
        return super(LogoutAPI, self).post(request, format=None)

class LogoutAllAPI(KnowLogoutAllView):
    def post(self, request):
        return super(LogoutAllAPI, self).post(request, format=None)

class UserDetailAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    def get_object(self):
        print(self.request.META)
        return get_object_or_404(User, pk=self.kwargs.get('id'))
