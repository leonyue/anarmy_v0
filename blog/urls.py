from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^index/',views.Index.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/',views.Post.as_view(),name='post'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^about/',views.about,name='about'),
    ]
