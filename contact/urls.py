from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('confirmation/', views.Index.as_view(), name='confirmation')
]