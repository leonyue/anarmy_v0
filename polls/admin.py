from django.contrib import admin

from .models import Question
from .models import Choice

#管理页布局修改
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['pub_date']}),
        ('Date information',{'fields':['question_text']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date','question_text']

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
