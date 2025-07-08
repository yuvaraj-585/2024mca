from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def yuvaraj(request):
    return render(request, 'yuvaraj.html')
def prasad(request):
    return render(request, 'prasad.html')