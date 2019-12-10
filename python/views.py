from django.shortcuts import render

# Create your views here.
def python(request):
    return render(request,'python/python.html')

def basic_python(request):
    return render(request,'python/basic_python.html')
