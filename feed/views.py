from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from accounts.models import Followers,FrontendUsers
from jit.models import Jit,Jit_Likedby
from accounts.models import FrontendUsers
# Create your views here.
def feed(request):
    if request.method  =='GET' and request.user.is_authenticated:

        user_detail = FrontendUsers.objects.get(username = request.user.username)

        context = {
            'profile' : user_detail,
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


    return redirect('signin')

        

def notifications(request):
    return redirect('accounts/signin')

def settings(request):
    return redirect('login')

def profile(request,user_id):
    if request.user.is_authenticated:
        profile = FrontendUsers.objects.get(id = user_id)
        if not profile:
            profile = get_object_or_404(FrontendUsers, id = request.user.id)
        jits = Jit.objects.all().filter(author = user_id).order_by('date')
        posts = jits.count()
        context = {
            'jits' : jits,
            'posts' : posts,
            'profile' : profile,
    
        }
    return render(request,'profile.html',context)


def check(request):
    userid = request.GET['user_id']
    jitid = request.GET['jit_id']


    boolean = str(Jit_Likedby.objects.filter(user_id_id = userid, jit_id_id = jitid).exists())
    print(boolean)
   # if boolean == True:
   #     result = 'True'
   # else:
   #     result = 'False'

    context = { 'liked' : boolean}

    return JsonResponse(context)

def search_user(request):
    q = request.GET['q']
    query = FrontendUsers.objects.filter(first_name__startswith=q).values("first_name")
    print(query)
    result = {
        'result':list(query)
    }

    return JsonResponse(result)

