from django.urls import path
from .import views

urlpatterns = [
    path("api/", polls_list, name="polls_list"),
    path("api/<int:pk>/", polls_detail, name="polls_detail")
    
