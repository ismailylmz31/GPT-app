from django.shortcuts import render



from myproject.myapp.permissions import IsOwner
from .models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import generics, pagination
from .permissions import IsOwner

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdminUser]

class ItemListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwner]
    pagination_class = pagination.PageNumberPagination


