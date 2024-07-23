from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error':'Username already exists'},status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        return Response({'success':'User created successfully'},status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'token': token},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)
            
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
    