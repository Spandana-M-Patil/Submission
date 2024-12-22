from django.shortcuts import render
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        return HttpResponseRedirect(f'/welcome/{username}')
    return render(request, 'login.html')

def welcome_view(request, username):
    return render(request, 'welcome.html', {'username': username})
