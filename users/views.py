from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    '''log out user'''
    logout(request)
    return redirect('learning_logs:index')

