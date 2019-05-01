
from django.urls import path
from game.views import *

app_name="game"

urlpatterns = [

    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('single/', single, name='single'),
    path('games/', games, name='games'),
    path('review/', review, name='review'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('search/', search, name='Search'),


]
