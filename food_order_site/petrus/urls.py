from django.urls import path
from petrus import views

urlpatterns = [
    path('', views.index, name='home'),
]
