from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('sugestoes', views.sugestoes_page_view, name='sugestoes'),
    path('localizacoes', views.localizacoes_page_view, name='localizacoes')
]