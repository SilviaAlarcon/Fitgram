#Users views

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Exception
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalidad username or password'})

    return render(request, 'users/login.html')


def signup_view(request):
    #The POST method is validated
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        #Password validation 
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        #Exception in case the username already exists 
        try:
            #User creation
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        #The remaining fields are added to the created user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email'] 
        user.save()

        #User profile is created 
        profile = Profile(user=user)     
        profile.save()  

        return redirect('login')

    return render(request, 'users/signup.html')


def update_profile(request):
    return render(request, 'users/update_profile.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login') 