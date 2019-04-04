from django.shortcuts import render, redirect
from accounts.models import Followers,FrontendUsers
from jit.models import Jit
# Create your views here.
def feed(request):
    if request.method  =='GET' and request.user.is_authenticated:

        user_detail = FrontendUsers.objects.get(username = request.user.username)

        context = {
            'logged_user' : user_detail,
        }

        followers = Followers.objects.values("follower_id").filter(following_id = user_detail.id)
        jit = Jit.objects.all()
        lis = []
        for x in followers:
            lis.append(jit.filter(author_id = x['follower_id']))
        show_jits = None
        
        if len(lis) != 0:
            for x in range(1,len(lis)):
                lis[0] = lis[0] | lis[x]
            show_jits = lis[0] 
        context.update({'jits' : show_jits})
        return render(request,'home.html',context=context)


    return render(request,'home.html')

        

def notifications(request):
    return redirect('accounts/signin')

def settings(request):
    return redirect('login')

def profile(request,user_id):
    if request.user.is_authenticated:
        jits = Jit.objects.all().filter(author = user_id).order_by('date')
        posts = jits.count()
        context = {
            'jits' : jits,
            'posts' : posts
        }
    return render(request,'profile.html',context)