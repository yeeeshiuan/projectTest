from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from account.forms import UserForm

    
def main(request):
    '''
    Main page
    '''
    template = 'account/main.html'
    return render(request, template)
    
def register(request):
    '''
    Register a new user
    '''
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm()})

    # POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm})

    userForm.save()
    return redirect('account:main')
    
def login(request):
    '''
    Login an existing user
    '''
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template)

    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        return render(request, template)

    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        return render(request, template)

    # login success
    auth_login(request, user)
    return redirect('account:main')