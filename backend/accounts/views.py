from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from .serializers import UserSerializer, LoginSerializer, UserProfileSerializer, ChangePasswordSerializer
from .models import UserProfile


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(
                raise_exception=True) and not request.user.is_authenticated:
            user = serializer.create(request.data)
            if user:
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(
                raise_exception=True) and not request.user.is_authenticated:
            user = serializer.login_user(data=data)
            token = RefreshToken.for_user(user)
            response_data = serializer.data
            response_data['tokens'] = {
                "refresh": str(token), "access": str(
                    token.access_token)}
            login(request, user)
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ViewMyProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        my_profile = UserProfile.objects.filter(user=request.user)
        serializer = UserProfileSerializer(my_profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ResetPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        user = request.user
        if serializer.is_valid(
                raise_exception=True) and user.check_password(
                serializer.data.get('old_password')):
            user.set_password(serializer.data.get('new_password'))
            user.save()
            update_session_auth_hash(request, user)
            return Response(
                {"message": "Password changes succesfuly"}, status=status.HTTP_200_OK)
        return Response({"error": "incorrect password"},
                        status=status.HTTP_400_BAD_REQUEST)
