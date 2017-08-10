from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogsPost

from django.views import generic

class Index(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/index.html"
    def get_queryset(self):
        return BlogsPost.objects.order_by('-timestamp')[:20]

def index(request):
    return HttpResponse("Blog Index page.")
