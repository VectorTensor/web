from django.urls import path
from . import views
app_name="QA"
urlpatterns=[
    path('',views.index,name="main"),
    path("<int:post_id>",views.post,name="posts")
   
    
]