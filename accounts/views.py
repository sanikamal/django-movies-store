from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    data = {}
    data['title'] = 'Sign Up'
    if request.method == 'GET':
        data['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html', {'data': data})
