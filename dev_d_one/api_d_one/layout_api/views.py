from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from .serializers import TodoSerializer, mainFeaturedPostSerializer, bodyPostSerializer, newsPostSerializer
from .models import Todos, mainFeaturedPost, bodyPost, newsPost
import os

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todos.objects.all()

class mainFeaturedPostView(viewsets.ModelViewSet):
    serializer_class = mainFeaturedPostSerializer
    queryset = mainFeaturedPost.objects.all()

class bodyPostView(viewsets.ModelViewSet):
    serializer_class = bodyPostSerializer
    queryset = bodyPost.objects.all()

class newsPost(viewsets.ModelViewSet):
    serializer_class = newsPostSerializer
    queryset = newsPost.objects.all()


    