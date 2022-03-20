from django.urls import path
from . import views

urlpatterns = [
    path('goal/', views.goal),
    path('defender/', views.defender),
    path('midfield/', views.midfield),
    path('forward/', views.forward),
    path('event/', views.forward)

]