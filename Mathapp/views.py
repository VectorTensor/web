from django.shortcuts import render
from .feat import linear_ALG
from .feat import mat
import numpy as np


# Create your views here.

def index(request):
    
    return render(request,'Mathapp/index.html')
def sub(request):
    if request.method=="POST":
        a11=int(request.POST["a11"])
        a12=int(request.POST["a12"])
        a13=int(request.POST["a13"])
        a21=int(request.POST["a21"])
        a22=int(request.POST["a22"])
        a23=int(request.POST["a23"])
        a31=int(request.POST["a31"])
        a32=int(request.POST["a32"])
        a33=int(request.POST["a33"])
        a=int(request.POST["a"])
        b=int(request.POST["b"])
        c=int(request.POST["c"])
        p=np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
        q=np.array([a,b,c])
       
        q1=linear_ALG(p,q)
        d=q1.solve()
        
        return render(request,'Mathapp/index.html',{
            "a":d[0],
            "b":d[1],
            "c":d[2]

   

    })


def rank(request):
    if request.method=="POST":
        a11=int(request.POST["a11"])
        a12=int(request.POST["a12"])
        a13=int(request.POST["a13"])
        a21=int(request.POST["a21"])
        a22=int(request.POST["a22"])
        a23=int(request.POST["a23"])
        a31=int(request.POST["a31"])
        a32=int(request.POST["a32"])
        a33=int(request.POST["a33"])
        a= np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
        q1=mat(a)
        c=q1.Rank()
        
        return render(request,'Mathapp/index.html',{
        "rank":c
        })
   

   

def eigen(request):
    if request.method=="POST":
        a11=int(request.POST["a11"])
        a12=int(request.POST["a12"])
        a13=int(request.POST["a13"])
        a21=int(request.POST["a21"])
        a22=int(request.POST["a22"])
        a23=int(request.POST["a23"])
        a31=int(request.POST["a31"])
        a32=int(request.POST["a32"])
        a33=int(request.POST["a33"])
        a= np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
        q1=mat(a)  
        c=q1.eign()
        return render(request,'Mathapp/index.html',{
        "eigen1":c[0],
        "eigen2":c[1],
        "eigen3":c[2]
        
        })
        
