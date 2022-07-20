from tkinter import E
from urllib import request, response
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Tournament, tournament_profile_rel, Invitation
from user_info.models import CustomUser
from rest_framework.permissions import AllowAny
from .serializer import TournamentSerializer, InvitationSerializer, TournamentViewSerializer
# from django.views.decorators.csrf import csrf_exempt

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
        to_user = CustomUser.objects.get(pk=request.data)
        tournament_request = Invitation.objects.get(from_user=from_user, to_user = to_user)
        response ={
            'sucess' : 'True',
            'message' : 'Request Sent Sucessfully'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    
    # def 


        # try:
        #     # tournament_request =Invitation.objects.filter(sender=request.user_id, receiver=receiver)
        #     # print(user_profile.age)
        #     Serializer = InvitationSerializer(tournament_request, many=False)
        #     try:
        #         for i in tournament_request:
        #             if i.is_active:
        #                 raise Exception("You already sent them a request")
        #         tournament_request = Invitation.objects.filter(sender=user, receiver=receiver)
        #         tournament_request.save()
        #         return Response("Tournament Request Sent")

        #     except Exception as e:
        #         return Response(str(e))
        # except tournament_request.DoesNotExit:
        #     tournament_request =Invitation.objects.filter(sender=user, receiver=receiver)
        #     tournament_request.save()
            # return Response("Send Tournament_request")
        
        

# @csrf_exempt
# class TournamentInviteView(CreateView):
    
#     serializer_class = TournamentInviteSerializer
#     permission_classes = (AllowAny,)


#     def post(self, request):  

#         data = {
#             'status':request.data.get('status'),
#             'tournament_id' : request.data.get('tournament_id'),
#         }
#         serializer =TournamentInviteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#             'success': 'true',
#             'message': 'User Register Successfully',
#             }
        
#             return Response(response , status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)