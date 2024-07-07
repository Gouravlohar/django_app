from django.urls import path

from .views import index,heart_predict,login,heart_result

urlpatterns = [
    path("", index,name="home"),
    path("heart_predict/", heart_predict,name="heart_predict"),
    path("heart_result/", heart_result,name="heart_result"),
    path("login/", login,name="login"),
]
