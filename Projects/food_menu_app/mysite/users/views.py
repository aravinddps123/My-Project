

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import RegistrationForm


def register(request):

    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        #check if the form is valid if it is valid then get user name and display success
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account has been successfully created' )
            return redirect('login')
    else:
        form = RegistrationForm()


    return render(request, 'users/register.html', {"form":form})


@login_required
def profilepage(request):

    return render(request, 'users/profile.html')
