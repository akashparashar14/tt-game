from rest_framework.views import APIView
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Tournament, tournament_profile_rel, Invitation
from user_info.models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializer import TournamentSerializer, InvitationSerializer, TournamentViewSerializer, UpdateTournamentSerializer

# Create your views here.

class TournamentAddAPI(APIView):

    serializer_class = TournamentSerializer
    permission_classes = (AllowAny,)

    def post (self, request, *args,**kwargs):
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'success': 'true',
            'message': 'User profile created successfully',
            'data': serializer.data
            }
        
            return Response(response , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class TournamentView(APIView):

    serializer_class = TournamentViewSerializer
    permission_classes = (AllowAny,)

    def get(self, request, pk = None, format=None):
        id = pk
        tournament_profile = Tournament.objects.get(pk=id)
        print(tournament_profile.tournament_name)
        serializer = TournamentSerializer(tournament_profile, many=False)
        response = {
                    'success': 'True',
                    'message': 'User profile fetched successfully',
                    'data': serializer.data  
                }
        return Response(response, status=status.HTTP_200_OK)


class InvitationView(APIView):
    def post(self, request, *args, **kwargs):
        from_user = request.user
        to_user = request.data['user_id']
        Invitation(from_user=from_user, to_user_id=to_user, tournament_id_id = request.data['tournament_id']).save()

        response ={
            'sucess' : 'True',
            'message' : 'Request Sent Sucessfully'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    
    
class InvitationStatusView(APIView):    
    def post(self, request):
        invitation_request = Invitation.objects.get(id=request.data['id'])
        print(invitation_request.to_user)
        
        if invitation_request:
            response ={
            'sucess' : 'True',
            'message' : 'Request Accepted Sucessfully'
        }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response ={
            'sucess' : 'False',
            'message' : 'Request Denied Sucessfully'
        }
            return Response(response, status=status.HTTP_200_OK)
        # if invitation_request.to_user == request.user:
        #     if invitation_request.is_accepted == True:
        #         return Response("You are in tournament")
        #     elif invitation_request.not_accepted == True:
        #         return Response("You denied for tournament")
        #     else:
        #         return Response("Pending")

class UpdateTournamentView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated ,)
    serializer_class = UpdateTournamentSerializer 
    
class DeleteTournament(APIView):
    def delete(self,request,pk=None,format=None):
        id = pk
        stu = Tournament.objects.get(pk=id)
        stu.delete()
        return Response({'mssg':'Data Deleted Succesfully'}, status = status.HTTP_204_NO_CONTENT)