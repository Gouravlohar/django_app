from django.urls import path

from .views import index,heart_predict,login

urlpatterns = [
    path("", index,name="home"),
    path("heart_predict/", heart_predict,name="heart_predict"),
     path("login/", login,name="login"),
]
