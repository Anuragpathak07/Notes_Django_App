from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',views.HomeView.as_view(),name="home"),
    path('login/',views.LoginInterfaceView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='/login/'),name="logout"),
    path('register/',views.SignupView.as_view(),name="register"),
]
