from django.urls import path
from .import views

urlpatterns = [
    path("Categories/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail")
]