from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render,redirect
from .forms import UserLoginForm
#from newsletter import templates

def login_view(request):
    title= "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect("/newsletter/articles")
    return render(request,"form.html", {"form":form,"title":title})


def logout_view(request):
    logout(request)
    return redirect("/newsletter/login")

    return render(request,"form.html", {})