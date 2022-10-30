from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('language', views.select_language, name='select_language')
]
