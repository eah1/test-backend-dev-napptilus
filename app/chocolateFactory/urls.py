from django.urls import path
from . import views

urlpatterns = [
    path(r'oompaLoompa/', views.OompaLoompaList.as_view()),
    path(r'oompaLoompa/<int:pk>/', views.OompaLoompaDetall.as_view()),
]
