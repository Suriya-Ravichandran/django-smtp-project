from django.urls import path
from . import views

app_name="smtp"

urlpatterns=[
    path("",views.index,name="index")
]