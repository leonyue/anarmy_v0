from django.contrib import admin
from .models import BlogsPost,UserExtra


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)
admin.site.register(UserExtra)
