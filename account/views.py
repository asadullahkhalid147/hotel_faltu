from django.shortcuts import render
from.forms import sinup_form
from django.contrib.auth import  login,logout,authenticate
from django.shortcuts import render,redirect
from .forms import sigin_form,userProfile
from django.contrib.auth.models import User

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def regisger(request):
    if request.method=="POST":
            form = sinup_form(request.POST) 
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('home')
                
    else:
            form =sinup_form()    
    return render (request,'singup.html',{'form':form})


def singout(request):
      logout(request)
      return redirect('home')





def login_veiw(request):
   if request.method=='POST':
       form =sigin_form(request.POST)
       print(request.POST)
       username = request.POST['username']
       password = request.POST['password']
       
       user = authenticate(username= username, password= password)
       if user is not None:
           login(request,user)
           return redirect('home')
   else : form =sigin_form()
   return render(request,'login.html',{'form':form})




def profile(request):
     user  = request.user
     if request.method == "POST":
          form  = userProfile(request.POST,instance=user)
          if form.is_valid():
               form.save()
          return redirect('home')
     else: form  = userProfile(instance=user)

     return render(request,'profile.html',{'form':form})





def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
          
            return redirect('home')
        else :return redirect('change_password')
       
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
