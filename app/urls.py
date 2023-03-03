from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("predict_api",views.predict_api),
]
