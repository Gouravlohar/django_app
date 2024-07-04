from django.urls import path

from .views import index,heart_predict

urlpatterns = [
    path("", index,name="home"),
    path("heart_predict/", heart_predict,name="heart_predict"),
]
