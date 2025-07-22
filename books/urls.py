
from django.urls import path
from . import views


urlpatterns = [
    path('',views.helo,name='helo'),
    path('home_page/',views.Home_page,name='home_page')

]