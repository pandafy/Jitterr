from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from accounts.models import Followers,FrontendUsers
from jit.models import Jit,Jit_Likedby
from accounts.models import FrontendUsers
# Create your views here.
def feed(request):
    if request.method  =='GET' and request.user.is_authenticated:
        try:
            user_detail = FrontendUsers.objects.get(username = request.user.username)
        except Exception:
            return redirect('signin')

    

        context = {
            'profile' : user_detail,
        }


        followers = Followers.objects.values("following_id").filter(follower_id = user_detail.id)
        jit = Jit.objects.all()
        lis = []
        for x in followers:
            lis.append(jit.filter(author_id = x['following_id']))
        show_jits = None
        
        if len(lis) != 0:

            for x in range(1,len(lis)):
                lis[0] = lis[0] | lis[x]
            show_jits = lis[0].order_by('-date') 
        context.update({'jits' : show_jits})

        return render(request,'home.html',context=context)


    return redirect('signin')

def follow(request):
    userID = str(request.GET.get('user_id'))
    followID = str(request.GET.get('follow_id'))
    context = {}

    try:
        followInst = Followers.objects.get(follower_id = userID, following_id = followID)
        followInst.delete()
        context.update({'following' : 'False'})
   
    except Followers.DoesNotExist:
        followInst = Followers.objects.create(follower_id = userID, following_id = followID)
        context.update({'following' : 'True'})

        followInst.save()
    
        

    return JsonResponse(context)


def notifications(request):
    context = {
        'profile' :getLoggecUser(request.user.id)
    }
    return render(request,'accounts/notifications.html',context)


def settings(request):
    context = {
        'profile' :getLoggecUser(request.user.id)
    }
    return render(request,'accounts/settings.html',context)

def profile(request,user_id):
    if request.user.is_authenticated:
        profile = FrontendUsers.objects.get(id = user_id)
        if not profile:
            profile = get_object_or_404(FrontendUsers, id = request.user.id)
        is_followed = str(Followers.objects.filter(follower_id = user_id, following_id = request.user.id ).exists())
        jits = Jit.objects.all().filter(author = user_id).order_by('date')
        posts = jits.count()
        context = {
            'jits' : jits,
            'posts' : posts,
            'profile' : profile,
            'is_followed' : is_followed
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
    query = FrontendUsers.objects.filter(first_name__startswith=q).values("first_name","id","avatar")
    print(query)
    result = {
        'result':list(query)
    }

    return JsonResponse(result)

def searchPage(request): 
    context = {'profile' : getLoggecUser(request.user.id) }

    userName = request.GET.get('search-user')

    users = FrontendUsers.objects.filter(first_name__contains = userName)

    for x in users:
        try:
            Followers.objects.get(follower_id = request.user.id, following_id = x.id)
            x.is_followed = "True"
        except Exception:
            x.is_followed = "False"
            continue
    context.update({'users' : users})

    return render(request,'search.html',context)

def getLoggecUser(userid):
    return FrontendUsers.objects.get(id = userid)

