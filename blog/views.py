from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogsPost

from django.views import generic

app_name = 'blog'

class Index(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/index.html"
    def get_queryset(self):
        return BlogsPost.objects.order_by('-timestamp')[:20]

class Post(generic.DetailView):
    model = BlogsPost
    context_object_name = "post"
    template_name = "blog/post.html"

def contact(request):
    return render(request,"blog/contact.html",{})

def about(request):
    return render(request,"blog/about.html",{})
