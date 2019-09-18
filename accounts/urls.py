from django.urls import path
from .views import *
urlpatterns = [

    path('login/',login, name='login'),
    path('home/',home, name='home'),
    path('signup/',signup, name='signup'),
    path('profile/',profile, name='profile'),
    path('editprofile/',edit_profile, name='editprofile'),
    path('logout/',mylogout, name='logout'),
    path('a/',aaa, name='aaa'),
    path('ind/',ind, name='ind'),
]
