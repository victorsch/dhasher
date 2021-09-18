from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('create_tests', views.create_initial, name="test"),

]