from django.shortcuts import render, redirect
from .models import Jit,Jit_Comment,Jit_Likedby
from django.contrib import messages
from accounts.models import FrontendUsers

# Create your views here.

def jit(request,jit_id):
    if request.method =='GET':
        allJits = Jit.objects
        jit = allJits.get(id = jit_id)
        context = {
                'focus':jit,
            }
        if (jit.is_reply == True):
            try:
                parent = Jit_Comment.objects.get(comment_id_id = jit.id)
                context.update({'parent' : parent})
                children = Jit_Comment.objects.filter(parent_id_id = parent.parent_id_id).exclude(comment_id_id =jit.id)
                context.update({'children' : children})
            except Exception as e :
                print(e)

            



           

    
    return render(request,'jits.html',context)

def new_post (request):
    if request.method == "POST":
        value = request.POST.get('value')

        if value != '' and value :
            author_id = int(request.POST['user_id'])
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