from django.urls import path
from pages import views

urlpatterns = [
    path('',views.home_page,name = 'home_page'),
]