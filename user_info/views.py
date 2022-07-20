from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializer import RegisterSerializer, UserSerializer, UpdateUserSerializer, ChangePasswordSerializer
from .models import CustomUser
from rest_framework import generics
from rest_framework import status


# Create your views here.
class RegisterView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'success': 'true',
            'message': 'User profile created successfully',
            }
        
            return Response(response , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ProfileView(APIView):


    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    
    def get(self, request):
        try:
            user_profile = CustomUser.objects.get(id=request.user.id)
            # print(user_profile.age)
            Serializer = UserSerializer(user_profile, many=False)
            response = {
                'success': 'True',
                'message': 'User profile fetched successfully',
                'data': Serializer.data  
            }
        except Exception as e:
            response = {
            'success' : 'False',
            'message': 'User profile not fetched successfully',
            }
        return Response(response, status=status.HTTP_404_NOT_FOUND)

class UpdateProfileView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated ,)
    serializer_class = UpdateUserSerializer   

class ChangePasswordView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

