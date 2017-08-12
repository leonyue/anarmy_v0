from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse,Strin
from django.forms.models import model_to_dict

from .models import BlogsPost

from django.views import generic

app_name = 'blog'

def countPlus(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    return request.session['count']

def resetCount(request):
    if 'count' in request.session:
        del request.session['count']

def moreposts(request):
    posts = BlogsPost.objects.order_by('-timestamp')[:2]
    jsonPosts = []
    for post in posts:
        jsonPost = model_to_dict(post)
        jsonPost['pk'] = post.pk
        jsonPosts.append(jsonPost)
    return JsonResponse(jsonPosts,safe=False)

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
