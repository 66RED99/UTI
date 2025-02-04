from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_uti, name='predict_uti'),
]