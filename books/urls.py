from django.urls import path,include
from . import views
from .views import PostApi
from rest_framework import routers
router =routers.DefaultRouter()
router.register('apiposts',PostApi)

urlpatterns = [
    path('home/',views.all_books, name='all_books'),
    path('details/<int:id>/',views.details, name='details'),
    path('add_post/',views.add_post, name='add_post'),
    path('api/',include(router.urls))
]