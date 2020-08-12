from django.shortcuts import render
from .models import Question
# Create your views here.
def index(request):

    posts= Question.objects.all()
    return render(request,'mainpage/index.html',{
        "posts":posts
    })


    

