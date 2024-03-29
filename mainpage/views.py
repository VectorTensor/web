from django.shortcuts import render
from .models import Question
from .models import Answer
from .models import comment
from django import forms

class NewQuestionForm(forms.Form):
    
    Q_photo=forms.ImageField(label="Image")

class NewAnswerForm(forms.Form):
  
    A_photo=forms.ImageField(label="Image")

class NewCommentForm(forms.Form):
    C_photo=forms.ImageField(label="Image")

# Create your views here.
def index(request):
    if request.method=="POST":
        form1=NewQuestionForm(request.POST,request.FILES)
        form2=NewAnswerForm(request.POST,request.FILES)
        if form1.is_valid():
            print("not valid")
            Q_photo=form1.cleaned_data["Q_photo"]

        if form2.is_valid():
            A_photo=form2.cleaned_data["A_photo"]
       
       # A_photo=form2.data.get("photo")
        
        Q_about=request.POST["Q_about"]
        A_about=request.POST["A_about"]
        m=Answer.objects.create(About=A_about,Image=A_photo,thumbsup=0)
        m.save()
        n=Question.objects.create(About=Q_about,Image=Q_photo,Primary_answer=m)
        n.save()

    posts= Question.objects.all()
    ans=Answer.objects.all()
    com=comment.objects.all()

    return render(request,'mainpage/index.html',{
        "posts":posts,
        "form1":NewQuestionForm,
        "form2":NewAnswerForm
       
        
    })

def post(request,post_id):
    if request.method=="POST":
        form=NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            C_photo=form.cleaned_data["C_photo"]

        C_about= request.POST["C_About"]   
        m=comment.objects.create(About=C_about,Image=C_photo,Question=Question.objects.get(pk=post_id))
        m.save()

    posts= Question.objects.get(pk=post_id)
    Comments=posts.Ques.all()
   
    return render(request,'mainpage/detail.html',{
        "post":posts,
        "Comments":Comments,
        "form":NewCommentForm

        
    })




    

