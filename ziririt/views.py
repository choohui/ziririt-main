from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def home(request):
    return render(request, 'home.html')

def credit(request):
    return render(request, 'credit.html')

def gumi(request):
    return render(request, 'gumi.html')

