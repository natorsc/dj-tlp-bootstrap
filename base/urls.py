from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
    path(route='', view=views.home, name='home'),
]
