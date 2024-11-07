from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(f"Form data: {request.POST}")
        
        if form.is_valid():
            print('Form is valid') # debugging print
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')