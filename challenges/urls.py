from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('exercises/', views.ListExcerciseView.as_view(), name='list-exercises'),
    path('exercises/<int:pk>/tasks/', views.DetailExcerciseView.as_view(), name='try-exercises'),
    path('exercises/<int:pks>/tasks/<str:identifier>/', views.ChallengeView.as_view(), name='do-challenge'),
]