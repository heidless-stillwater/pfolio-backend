from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import App
from .serializers import AppSerializer


class AppListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = App.objects.all()
    serializer_class = AppSerializer
    pagination_class = None
