from django.shortcuts import render

def index(request):
    data = {}
    data['title'] = "Rua's Movies Store"
    return render(request, 'main/index.html',{'data':data})

def about(request):
    data = {}
    data['title'] = "About Us"

    return render(request, 'main/about.html',{'data':data})
