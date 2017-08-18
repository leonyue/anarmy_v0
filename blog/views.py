from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BlogsPost

from django.views import generic

# 更多计数
def countPlus(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    return request.session['count']

# 重制更多计数
def resetCount(request):
    if 'count' in request.session:
        del request.session['count']

# 更多数据源
class MorePost(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/morepost.html"
    def get_queryset(self):
        count = countPlus(self.request)
        return BlogsPost.objects.order_by('-timestamp')[5 * count:5 * (count+1)]

class About(generic.DetailView):
    context_object_name = "userextra"
    template_name = "blog/about.html"


# Index数据源
class Index(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/index.html"
    def get_queryset(self):
        resetCount(self.request)
        return BlogsPost.objects.order_by('-timestamp')[:5]

class Post(generic.DetailView):
    model = BlogsPost
    context_object_name = "post"
    template_name = "blog/post.html"

def contact(request):
    return render(request,"blog/contact.html",{})

def about(request):
    # userid = request.GET.get('userid',0)
    user = User.objects.get(username='dj.yue')
    print("user :",user)
    return render(request,"blog/about.html",{"user":user})
