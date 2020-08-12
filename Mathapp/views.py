from django.shortcuts import render
from .feat import linear_ALG
from .feat import mat
import numpy as np


# Create your views here.

def index(request):
    return render(request,'Mathapp/index.html')


def calc_1(request):
    a=np.array([[1,1],[1,-1]])
    b=np.array([[1],[1]])
    c=np.array([[0],[0]])
    q1=linear_ALG(a,b)
    c=q1.solve().astype(int)
    
    
    return render(request,'Mathapp/index.html',{
        "a":c[0,0],
        "b":c[1,0]
    })

def calc_2(request):
    a= np.array([[1,1],[3,5]])
    q1=mat(a)
    c=q1.Rank()
    return render(request,'Mathapp/index.html',{
        "rank":c
    })


def calc_3(request):
     a= np.array([[1,1],[3,5]])
     q1=mat(a)   
     c=q1.eign()
     return render(request,'Mathapp/index.html',{
        "eigen1":c[0],
        "eigen2":c[1]
        
    })
