from django.urls import path
from . import views

app_name="Math"

urlpatterns=[
    path('',views.index,name="index"),
     path('calc_1',views.calc_1,name="eqn_sol"),
     path('calc_2',views.calc_2,name="rank"),
     path('calc_3',views.calc_3,name="eigen")
]