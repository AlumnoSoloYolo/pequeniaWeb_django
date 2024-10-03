from django.urls import path
from . import views

urlpatterns = [
    path('animal_list', views.animal_list, name='animal_list'),
    path('colaborador_list', views.colaborador_list, name='colaborador_list'),
    path('protectora_list', views.protectora_list, name='protectora_list'),
]
