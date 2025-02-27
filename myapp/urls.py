from django.urls import path
from . import views

urlpatterns = [
    path("lifeispython", views.lifeispython),
    path("uploadanywhere",views.uploadanywhere),
    path("claimbutton",views.claimbutton),
    path("home",views.home)
]

