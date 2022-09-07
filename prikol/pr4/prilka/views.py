from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

def home(request):
    return render(request , "home.html")

def about(request):
    return render(request , "about.html")


