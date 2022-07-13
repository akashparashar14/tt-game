from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer
from .models import CustomUser
import jwt


# Create your views here.
class RegisterView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': 'true',
            'message': 'User profile fetched successfully',
            }
        
        return Response(response)


class ProfileView(APIView):


    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            print(request.user)
            user_profile = CustomUser.objects.get(id=request.user.id)
            response = {
                'success': 'True',
                'message': 'User profile fetched successfully',
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                }]
            }

        except Exception as e:
            response = {
            'success' : 'True',
            'message': 'User registered  successfully',
            }
        return Response(response)

# class ProfileView(APIView):

#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = CustomUser.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)