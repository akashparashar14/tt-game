from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer, UpdateUserSerializer
from .models import CustomUser
from rest_framework import generics


# Create your views here.
class RegisterView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'success': 'true',
            'message': 'User profile created successfully',
            }
        
            return Response(response)
        return Response(serializer.errors)


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
            'message': 'User registered  successfully',
            }
        return Response(response)

class UpdateProfileView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UpdateUserSerializer     