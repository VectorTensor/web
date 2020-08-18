from django.urls import path
from . import views

app_name="Mathapp"

urlpatterns=[
    path('',views.index,name="index"),
  
    path('rank',views.rank,name="rank"),
    path('eigen',views.eigen,name="eigen"),
    path('sub',views.sub,name="sub")
]