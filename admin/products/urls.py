from django.contrib import admin
from django.urls import path
from .views import ProductViewSet, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'products', ProductViewSet)

urlpatterns = [
    path("user", UserViewSet.as_view({"get": "get"}))
]

urlpatterns += router.urls