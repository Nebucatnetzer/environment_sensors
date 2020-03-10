from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('history/<int:hours>', views.history_view, name='history'),
]
