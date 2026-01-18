from django.urls import path
from .views import helloViews

urlpatterns = [
    path('', helloViews, )
]