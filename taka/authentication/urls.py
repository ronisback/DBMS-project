from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.registration, name="register"),
    path('login/',views.LoginView, name="login"),
    path('logout/',views.logoutView, name="logout"),
    path('home/',views.home_page, name="home"),
]
