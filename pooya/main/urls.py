from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name = 'homeview'),
    # path('contact/', views.contact, name='contact'),
]