from django.urls import path
from . import views

app_name="Math"

urlpatterns=[
    path('',views.index,name="index"),
     path('calc',views.calc,name="calc")
]