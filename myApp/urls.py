from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_teams_by_league, name='index'),
]
