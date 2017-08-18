from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

def index(reqyest):
    return HttpResponseRedirect(reverse("blog:index",args=()))
