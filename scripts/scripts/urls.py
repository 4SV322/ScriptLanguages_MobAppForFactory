from django.contrib import admin
from django.urls import path
from app.views import AccountViewSet

urlpatterns = [
    path('accounts/', AccountViewSet.as_view({'get': 'list', 'post': 'create'}), name='accounts'),
    path('accounts/<int:pk>/', AccountViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account'),
]
