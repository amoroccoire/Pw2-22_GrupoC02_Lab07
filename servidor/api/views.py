from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from producto.models import Producto
from .serializers import ProductoSerializer

# Create your views here.

class ProductoListApiView(APIView):

    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'), 
            'categoria': request.data.get('categoria'),
            'tipo': request.data.get('tipo'),
            'precio': request.data.get('precio'),
            'disponible': request.data.get('disponible'),
            'imagen': request.data.get('imagen'),
        }
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)