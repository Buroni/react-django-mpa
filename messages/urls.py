from django.urls import path

from . import views

app_name = 'messages'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.MessageDetailView.as_view(), name='detail'),
]