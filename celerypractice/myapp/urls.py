from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('stud/<int:count>', stud, name='add'),
    path('delete/', delete, name='delete'),
]
