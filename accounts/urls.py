from . import views
from django.conf.urls import url

urlpatterns = [
    url("register", views.register,name="register"),
    url("login",views.login, name="login"),
    url("logout",views.logout, name="logout")
]