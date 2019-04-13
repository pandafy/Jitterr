from django.shortcuts import render, redirect
from .models import FrontendUsers
from django.contrib import messages, auth
from .models import FrontendUsers,Followers
from django.core.files.storage import FileSystemStorage


# Create your views here.
def signup(request):
    if request.method == 'POST' and request.FILES['avatar'] :
        avatar = request.FILES['avatar']
        fs = FileSystemStorage()
        filename = fs.save(avatar.name, avatar)
        uploaded_file_url = fs.url(filename)

        name = request.POST['name']
        if ' ' in name: 
            first_name = name.split(' ')[0]
            last_name = name.split(' ')[1]
        else:
            first_name = name
            last_name = ''
        username = request.POST['username']
        bio = request.POST['bio']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        avatar = uploaded_file_url

        #checks if passwords are correct

        if password1 == password2:
            #check whether username exists
            users = FrontendUsers.objects.filter(username = username)
            if users.exists():
                messages.error(request,'Username already taken')

            else:
                createdUser = FrontendUsers.objects.create_user(first_name = first_name,last_name= last_name,  username = username, bio = bio,password = password1, avatar = avatar)
                createdUser.save()
                follow = Followers.objects.create(follower_id= createdUser.id, following_id = createdUser.id)
                return redirect('signin')
        else:
            messages.error(request,'Passwords do not match ')
   
    return render(request,'accounts/signup.html')

def signin(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            
            return redirect('feed')
        else:
            messages.error(request,'Username or password is incorrect')

        
    return render(request,'accounts/signin.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You have been successfully logged out.')
        return redirect('feed')


