from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newgame', views.newgame, name='newgame'),
    path('enter', views.enter, name='enter'),
    path('balot', views.balot, name='balot'),
    path('deletegame', views.deletegame, name='deletegame'),
    path('deleteall', views.deleteall, name='deleteall'),
    path('winner', views.winner, name='winner'),
    path('definitions', views.definitions, name='definitions'),
    path('terms', views.terms, name='terms'),
    path('boards', views.boards, name='boards'),
]