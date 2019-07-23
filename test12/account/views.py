from django.shortcuts import render, redirect

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