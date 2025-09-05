from django.shortcuts import render

def home(request):
    return render(request, 'party/home.html')

def cake(request):
    return render(request, 'party/cake.html')

def timeline(request):
    return render(request, 'party/timeline.html')

def wish(request):
    return render(request, 'party/wish.html')
