from django.urls import path
from . import views

urlpatterns = [
        path('sample', views.sample, name =''),
        path('get_user/', views.get_user, name=''),
        path('leaderboard/', views.leaderboard, name=''),
        path('query_database', views.external_query_database, name ='')
            ]

