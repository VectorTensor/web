from django.shortcuts import render
from .models import Question
from .models import Answer
from .models import comment
# Create your views here.
def index(request):

    posts= Question.objects.all()
    ans=Answer.objects.all()
    com=comment.objects.all()

    return render(request,'mainpage/index.html',{
        "posts":posts
       
        
    })

def post(request,post_id):
    posts= Question.objects.get(pk=post_id)
   
    return render(request,'mainpage/detail.html',{
        "post":posts
        

        
    })




    

