from django.shortcuts import render

# Create your views here.

def conditions(request):
   d={'name':'saicharan','age': 10,'Gender':'male'}
   return render(request,'conditions.html',context=d)
