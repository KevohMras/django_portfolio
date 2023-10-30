from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name='portfolio'),
    path('data/', views.data, name='data'),
    path('add', views.add, name="add"),
    path('data', views.data, name="data")
]