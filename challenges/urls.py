from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListExcerciseView.as_view(), name='list-exercises'),
    path('<int:pk>/tasks/', views.DetailExcerciseView.as_view(), name='try-exercises'),
    path('<int:pks>/tasks/<str:identifier>/', views.ChallengeView.as_view(), name='do-challenge'),
]