from django.shortcuts import render, redirect # we import redirect to redirect the user when it is authenticated
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):
    page= 'login'   
    if request.user.is_authenticated: # if the user logs in redirect to profiles page 
        return redirect('profiles')
    
   
    if request.method == "POST": #first chaeck weather the request is post or not
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username) # check if the username exists in the database
   
        except: # we check if the user doesnt exist
                         
            messages.error(request, "User doesn't exist")
            
        user= authenticate(request, username=username, password=password) #what this function does is check if the password and username matches or not in the database
             
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")
        
            
    return render(request, "users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'User account was created!')
            
            login(request, user)
            return redirect('profiles')
            
        else:
            messages.success(request, 'An error has ocurred during registration!')    
            
    context= {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
   profile = Profile.objects.get(id=pk)
   
   topSkills = profile.skill_set.exclude(description__exact ="")
   otherSkills = profile.skill_set.filter(description = "")
   
   context = {'profile':profile, 'topSkills': topSkills, 'otherSkills': otherSkills} 
   return render(request, 'users/user-profile.html', context)

@login_required(login_url='login') # to access this page the user must login
def userAccount(request):
    profile = request.user.profile
    
    topSkills = profile.skill_set.exculude(description__exact ="")
    otherSkills = profile.skill_set.filter(description = "")
    context = {'profile': profile, 'topSkills':topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/account.html', context)