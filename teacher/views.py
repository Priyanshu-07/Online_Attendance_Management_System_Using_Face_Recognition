from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2 :
            myuser = User.objects.create_user(username, email, password1)


            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()
            messages.success(request, " You have successfully registered!")
            return redirect('../login')

        else:
            messages.error(request, "Password dont match ")
            print("password doesnt match")


    return render (request=request, template_name="registration/registration.html")