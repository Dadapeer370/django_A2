from django.shortcuts import render

# Create your views here.
def conditionalst(request):
    d={'name':'devil','age':17}
    return render(request,'conditionalst.html',d)