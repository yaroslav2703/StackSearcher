from django.urls import path
from search import views

urlpatterns = [
    path('', views.show_time, name='time'),
    path('exception/', views.show_exception, name='exception'),
]
