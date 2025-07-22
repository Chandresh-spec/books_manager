
from django.urls import path
from . import views


urlpatterns = [
    path('',views.helo,name='helo'),
    path('home_page/',views.Home_page,name='home_page'),
    path('register/',views.register_view,name='register_view'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login')

]