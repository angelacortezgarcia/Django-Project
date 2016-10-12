from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())


    context= {
        "form": form,
    }
    return render(request,"post_form.html", context)

def post_detail(request,id=None): #retrienve
    instance=get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request,"post_detail.html", context)

def post_list(request): #list items
    queryset = Post.objects.all().order_by('-timestamp')[0:3]
    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request,"post_list0.html", context)
    # return render(request,"index.html", context)

def post_articles(request): #list items
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 6) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request,"articels.html", context)
    # return render(request,"post_list.html", context)


def post_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"<a href='#'>Saved</a>",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request,"post_form.html", context)

def post_delete(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request,"successfully deleted")
    return redirect("newsletter:list")
