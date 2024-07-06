from django.shortcuts import render, HttpResponse
# Create your views here.
def index (request):
    return render(request,'index.html')
def heart_predict(request):
    return render(request,'heart_predict.html')
def login(request):
    return render(request,'login.html')
