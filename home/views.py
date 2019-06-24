from django.shortcuts import render
def home_view(request):
    return render(request,'home1.html')
def home_view1(request):
    return render(request,'login.html')
def home_view2(request):
    return render(request,'signup.html')
# Create your views here.
