from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import  viewsets
from rest_framework import status
from .serializer import *
from .models import *
from django.utils import timezone
from datetime import date,timedelta
from rest_framework import generics, mixins
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import *
from rest_framework.decorators import *
from rest_framework.permissions import *
from django.db import IntegrityError


#@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
#@permission_classes([AllowAny])
@api_view(['post'])
#1
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = User.objects.create_user(
            email=request.data["email"],
            username=request.data["username"],
            password=request.data["password"],
            )
        if user is not None:
            user.save()
            info_user = userInfo(user=user,
             national_number=request.data["national_number"],
             phone=request.data["phone"],
             email=request.data["email"],
             username=request.data["username"],
             password=request.data["phone"],
             )
            if info_user:
                info_user.save()
                token =Token.objects.create(user=user)
            return Response(token.key)
            # info_user.save()
            # user.save()
            # Token.objects.create(user=user)
            # if user :
            #     return Response("done")
            # else :
            #     return Response("wrong")

        

#2
@api_view(['POST'])
def get_user_info(request):
    usre_name = request.data['username']
    password = request.data['password']
    user = authenticate(username=usre_name, password=password)
    if user is not None:
        token = Token.objects.get(user_id=user)
        print(user)
        info= userInfo.objects.get(user=user)
        print(info)
        return Response({
            token.key,
        })
    else:
        return Response("Incorrect username or password")

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])   
@api_view(['POST'])
def notification_date(request):
    card_insantse = card.objects.get(id=request.data['id'])
    if card_insantse is not None:
        return Response({
            'date_of_expiry':card_insantse.date_of_expiry,
        })

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])   
@api_view(['POST'])
def accept_card(request):
    card_insantse = card.objects.get(id=request.data['id'])
    card_insantse.statu="accept"
    card_insantse.date_of_accept=date.today()
    card_insantse.save()
    if card_insantse is not None:
        return Response("success")

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])   
@api_view(['POST'])
def reject_card(request):
    card_insantse = card.objects.get(id=request.data['id'])
    card_insantse.statu="reject"
    card_insantse.date_of_reject=date.today()
    card_insantse.save()
    if card_insantse is not None:
        return Response("success")

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])   
@api_view(['POST'])
def anything(request):
    card_instance = card.objects.filter(card_date__gt=(request.data["start_date"]),card_date__lt=(request.data["end_date"]),card_center=request.data["center"],statu=request.data['status'])
    print(card_instance)
    if card_instance is not None:
            cards_counter=0
            data =[]
            for x in card_instance:
                cards_counter=cards_counter+1
                field ={
                   "FirstName": x.FirstName,
                   "SecondName": x.SecondName,
                   "Number_of_cards":cards_counter
                }
                data.append(field)
            return Response(data)

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])      
@api_view(['POST'])
def card_info(request):
    if request.method =='POST':
        today =date.today()
        expiry_date=date.today()+ timedelta(days=5*365)
        card_Instance = card(
        card_user=request.user,

        card_center=request.data["center"],
        FirstName=request.data["FirstName"],
        SecondName=request.data["SecondName"],
        ThirdName=request.data["ThirdName"],
        FourtName=request.data["FourtName"],
        Birthdate=request.data["Birthdate"],
        Placeof_Birth=request.data["Placeof_Birth"],
        Blood_Type=request.data["Blood_Type"],
        Job=request.data["Job"],
        Address=request.data["Address"],
        Phone=request.data["Phone"],
        Old_id=request.data["Old_id"],
        date_of_expiry=expiry_date,
        
        )


        try:
            if card_Instance:
                card_Instance.save()
                return Response("Done")
            else:
                return Response("wrong")
        except IntegrityError as e :
            print(card_Instance.date_of_expiry)
            print(today)
            if card_Instance.date_of_expiry < today:
                card_Instance.date_of_expiry=card_Instance.date_of_expiry+ timedelta(days=5*365)
                card_Instance.save()
                return Response("success")
            else :
                return Response("card is active")
                
                    
                         
    else:
        return Response("is get")

    

   

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])         
@api_view(['POST'])
def Payment_confirmation(request):
        payment_instance = Payment.objects.filter(process_number=request.data["process_number"])
        data = []
        for x in payment_instance:
            field = {
                "name": x.card.FirstName,
                "payment_date": x.payment_date,
                "payment_Notification" : payment_Notification,
            }
            data.append(field)

        return Response(data)
        

           

@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])         
@api_view(['POST'])
def Payment_infos(request):
    user= User.objects.get(id=request.user.id)
    card_instance = card.objects.get(card_user=user)
    print(card_instance)
    payment_Instance = Payment(
        payment_Notification=request.FILES['payment_Notification'],
        process_number=request.data["process_number"],
        card=card_instance,
        ) 

    if payment_Instance:
        payment_Instance.save()
    return Response("done")

        
  
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])      
@api_view(['GET'])
def get_user_request(request):
    #get all user card renew request
    cards= card.objects.all()
    if cards is not None:
        myrequest= card.objects.all()
        #array to append field
        data =[]
        
        for x in myrequest:
            #get user "FirstName",SecondName,"ThirdName","FourtName" from card 
            field = {
                "FirstName": x.FirstName,
                "SecondName":x.SecondName,
                "ThirdName": x.ThirdName,
                "FourtName": x.FourtName,
            }
            #append  field
            data.append(field)
            #Response data in api
        return Response(data)
#6
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])  
@api_view(['GET'])
def get_user_datails(request):
   details_id=card.objects.all()
   serializer=CardSerializer(details_id,many=True)
   return  Response(serializer.data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])  
@api_view(['POST'])
def show_my_report(request):
        serializer=reportSerializer(data=request.data)
        if serializer.is_valid():
            start_date = str(request.data["start_date"])
            end_date = str(request.data["end_date"]) 
            card_instance = card.objects.filter(card_date__gt=start_date,card_date__lt=end_date,card_center=str(request.data["center"]))
            cards_counter=0
            
            data =[]
            for x in card_instance:
                cards_counter=cards_counter+1
                field ={
                   "FirstName": x.FirstName,
                   "SecondName": x.SecondName,
                   "Number_of_cards":cards_counter
                }
                data.append(field)
            return Response(data)
           
# class CBV_List(APIView):
#     def get(self, request):
#         cards = card.objects.all()
#         serializer = CardSerializer(cards, many = True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = CardSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.data,
#             status= status.HTTP_400_BAD_REQUEST
#         )
# class  CBV_pk(APIView):

#     def get_object(self, pk):
#         try:
#             return card.objects.get(pk=pk)
#         except card.DoesNotExists:
#             raise Http404
#     def get(self, request, pk):
#         card = self.get_object(pk)
#         serializer = CardSerializer(card)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         card = self.get_object(pk)
#         serializer = CardSerializer(card, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         card = self.get_object(pk)
#         card.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
