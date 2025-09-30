# Create your views here.
from django.shortcuts import render
from django.http import    HttpResponse
def home(request):
    return render(request, 'login/index.html')

def login_view(request):
    return render(request, 'login/login.html')