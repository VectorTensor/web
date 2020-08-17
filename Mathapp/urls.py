from django.urls import path
from . import views

app_name="Mathapp"

urlpatterns=[
    path('',views.index,name="index"),
  
     path('calc_2',views.calc_2,name="rank"),
     path('calc_3',views.calc_3,name="eigen"),
     path('sub',views.sub,name="sub")
]