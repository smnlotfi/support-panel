from django.shortcuts import render
from django.contrib.auth.models import User
from .models import user_voipecode
from .forms import add_user,edit_user
from django.contrib.auth import authenticate
from django.http import JsonResponse


# Create your views here.

def users(request):

    
    edit_form=edit_user(request.POST or None)
    add_form=add_user(request.POST or None)

    # add_user
    
    if request.is_ajax():
        
        if request.POST:
            if request.POST('get_users'):
                 users=User.objects.all()
                 for user in users:
                    user.voipe_code=user_voipecode.objects.filter(user=user.id).first()   
                    user.is_admin=user_voipecode.objects.filter(user=user.id).first()
                 response=users

            else:
                username=request.POST.get('username')
                firstname=request.POST.get('firstname')
                voipe_code=request.POST.get('voipe_code')
                password=request.POST.get('password')
                user_role=request.POST.get('user_role')
                is_admin=True if user_role =='admin' else False
                user=User.objects.create_user(username=username,password=password)
                user.save()
                user.first_name=firstname
                user.is_active=True
                user.save()
                user=user_voipecode.objects.create(user_id=user.id,voipe_code=voipe_code,is_admin=is_admin)
                response=JsonResponse({'msg':'کاربر با موفقیت اضافه شد.'})
        return response

    
    # get all user
    
    users=User.objects.all()
    for user in users:
        user.voipe_code=user_voipecode.objects.filter(user=user.id).first()   
        user.is_admin=user_voipecode.objects.filter(user=user.id).first() 

    context={
        'users':users,
        'edit_form':edit_form,
        'add_form':add_form
    }

    return render(request,'users.html',context)