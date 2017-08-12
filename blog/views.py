from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import BlogsPost

from django.views import generic

def countPlus(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    return request.session['count']

def resetCount(request):
    if 'count' in request.session:
        del request.session['count']

class MorePost(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/morepost.html"
    def get_queryset(self):
        print("Into More post")
        return BlogsPost.objects.order_by('-timestamp')[:2]

class Index(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/index.html"
    def get_queryset(self):
        resetCount(request= self.request)
        return BlogsPost.objects.order_by('-timestamp')[:2]

class Post(generic.DetailView):
    model = BlogsPost
    context_object_name = "post"
    template_name = "blog/post.html"

def contact(request):
    return render(request,"blog/contact.html",{})

def about(request):
    return render(request,"blog/about.html",{})
