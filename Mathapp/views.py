from django.shortcuts import render
from .feat import linear_ALG
import numpy as np


# Create your views here.

def index(request):
    return render(request,'Mathapp/index.html')


def calc(request):
    a=np.array([[1,1],[1,-1]])
    b=np.array([[1],[1]])
    c=np.array([[0],[0]])
    q1=linear_ALG(a,b)
    c=q1.solve().astype(int)
    
    
    return render(request,'Mathapp/index.html',{
        "a":c[0,0],
        "b":c[1,0]
    })