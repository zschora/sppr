from django.urls import path
from . import views

urlpatterns = [
  path('predict/', views.PredictView.as_view(), name='predict'),
  path('result/', views.ResultView.as_view(), name='result'),
  path('', views.RandomArtistView.as_view()),
]