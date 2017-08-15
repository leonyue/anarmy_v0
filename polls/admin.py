from django.contrib import admin

from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
