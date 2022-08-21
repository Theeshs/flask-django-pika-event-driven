from random import random
from django.views import View
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
import random
from rest_framework import status

from products.models import Products, User
from .serializers import ProductSerializer

from products.producer import publish

class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        # publish()
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_created", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def update(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serialier = self.serializer_class(instance=product, data=request.data)
        serialier.is_valid(raise_exception=True)
        publish("product_updated", serialier.data)
        return Response(serialier.data, status=status.HTTP_202_ACCEPTED)
    

    def destroy(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        publish("product_deleted", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(ViewSet):
    
    def get(self, _):
        users = User.objects.all()
        if users is None or len(users) < 1:
            users = [
                {"id": 1},
                {"id": 2},
                {"id": 3},
                {"id": 4},
                {"id": 5}
            ]
        user = random.choice(users)
        return Response(
            {
                'id': user["id"]
            }
        )