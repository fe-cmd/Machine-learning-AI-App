from django.urls import path
from .import views

urlpatterns = [
    path('', views.begin, name='begin'),
    path('machine-learning/', views.index, name='dashboard-index'),
    path('predictions/', views.predictions, name='dashboard-predictions'),
]
