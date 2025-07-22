from django.shortcuts import render
from django.core.paginator import Paginator
from main.serializer import PeopleSerializer,LoginSerializer,RegisterSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from main.models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User















class PersonAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(request,self):
        objs=Person.objects.filter(color__isnull=False)
        page=request.GET.get('page',1)
        page_size=3
        paginator=Paginator(objs,page_size)
        print(paginator.page(page))
        

        serializer=PeopleSerializer(paginator.page(page),many=True)
        return Response(serializer.data)
       
    def post(request,self):
        data=request.data
        serializer=PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    def put(request,self):
        data=request.data
        serializer=PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
       
    def patch(request,self):
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(obj,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    
    def delete(request,self):
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})
    




class RegisterAPI(APIView):
    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=data)
        
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors,

            },status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({
                'status':True,
                'message':"user registered",

            },status=status.HTTP_201_CREATED)





class LoginAPI(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors,

            },status=status.HTTP_404_NOT_FOUND)
        print(serializer.data)

        
        user=authenticate(username=serializer.data['username'],password=serializer.data['password'])
        if not user:
             return Response({
                'status':False,
                'message':"invalid cred",

            },status=status.HTTP_404_NOT_FOUND)

        token=        Token.objects.get_or_create(user=user) 

        return Response({
                'status':True,
                'message':"user logged in",
                'token':str(token)

            },status=status.HTTP_201_CREATED)

