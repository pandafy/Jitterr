from django.shortcuts import render, redirect
from .models import Jit,Jit_Comment,Jit_Likedby
from django.contrib import messages
from accounts.models import FrontendUsers
from django.http import JsonResponse
# Create your views here.

def jit(request,jit_id):
    if request.method =='GET':
        allJits = Jit.objects
        jit = allJits.get(id = jit_id)
        context = {
                'profile' : FrontendUsers.objects.get(username = request.user.username),
            }
        if (jit.is_reply == True):
            try:
                parent = Jit_Comment.objects.get(comment_id_id = jit.id)
                context.update({'parent' : parent})
                context.update({'focus': jit})
                children = Jit_Comment.objects.filter(parent_id_id = parent.parent_id_id).exclude(comment_id_id =jit.id)
                context.update({'children' : children})
            except Exception as e :
                print(e)
        else:
            context.update({'parent' : jit})

            children = Jit_Comment.objects.filter(parent_id_id = jit_id)
  
            context.update({'children' : children})
                

    
    return render(request,'jits.html',context)

def new_post (request):
    if request.method == "POST":
        value = request.POST.get('value')

        if value != '' and value :
            print(request.POST)
            author_id = request.POST.get('user_id_js')
            
            jit = Jit.objects.create(value = value,author_id=author_id)
            jit.save()
            return redirect('feed')
        else:
            messages.error(request,'There was some problem writing your jit.')
    return redirect('feed')

def new_post1(request):
    if request.method == 'POST':
        if request.POST['is_reply'] == "True":
            value = request.POST.get('value')
            if value != '' and value :
                author_id = int(request.POST['user_id'])
                is_reply = True
                if request.POST['parent_id']:
                    parent_id = request.POST['parent_id']
                else:
                    parent_id = request.POST['focus_id']
                
                jit = Jit.objects.create(value = value,author_id=author_id,is_reply=is_reply)
                print(jit.id)
                jit_comment = Jit_Comment.objects.create(parent_id_id = parent_id,comment_id_id = jit.id)
                jit_comment.save()
                jit.save()
                return redirect('profile',user_id = request.user.id)
            else:
                messages.error(request,'There was some problem writing your jit.')
        else:
            messages.error(request,'Snaps')
            return redirect('feed')

def liked(request):
    
    userId = request.GET['userid']
    jitid = request.GET['jitid']
    print(userId,jitid)
    try:
        if Jit_Likedby.objects.filter(user_id_id = userId).exists():
            Jit_Likedby.objects.filter(user_id_id = userId).delete()
        else:
            like = Jit_Likedby.objects.create(user_id_id = userId, jit_id_id = jitid)
            like.save()
        #updation in liked_by 
        no_of_likes = Jit_Likedby.objects.filter(jit_id = jitid).count()
        data = {'likes' : no_of_likes}
        
        #updation in core Jit
        
        jit = Jit.objects.get(id = jitid)
        jit.likes = no_of_likes
        jit.save()


        return JsonResponse(data)
    except Exception as e:
        print(e)
        return JsonResponse('')