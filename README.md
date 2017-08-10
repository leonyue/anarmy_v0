project vs app
https://docs.djangoproject.com/en/1.11/intro/tutorial01/
http://blog.csdn.net/dbanote/article/details/11271115

#polls程序 创建新model
1\python manage.py makemigrations polls
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

polls/migrations/0001_initial.py
you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.


python manage.py sqlmigrate polls 0001
2\python manage.py migrate
Now, run migrate again to create those model tables in your database:

#shell模式
python manage.py shell
#model的使用
https://docs.djangoproject.com/en/1.11/intro/tutorial02/

#django管理员
##创建超级用户
python manage.py createsuperuser
##使poll应用在admin中可修改
polls/admin.py
from django.contrib import admin
from .models import Question
admin.site.register(Question)

#带参数的view
如 def vote(request, question_id):
url pattern写法url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

#模版Template
##目录结构 （官方建议在每个app的templates下再建一个app名的目录，以下第三段）
Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.
Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html. In other words, your template should be at polls/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django simply as polls/index.html.
Now we might be able to get away with putting our templates directly in polls/templates (rather than creating another polls subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the easiest way to ensure this is by namespacing them. That is, by putting those templates inside another directory named for the application itself.
##使用模板
方法1、
from django.template import loader
template = loader.get_template('polls/index.html')
context = {
'latest_question_list': latest_question_list,
}
return HttpResponse(template.render(context, request))

方法2、A shortcut: render()
from django.shortcuts import render
return render(request, 'polls/index.html', context)


#Raising a 404 error
普通方法
def detail(request, question_id):
try:
question = Question.objects.get(pk=question_id)
except Question.DoesNotExist:
raise Http404("Question does not exist")
return render(request, 'polls/detail.html', {'question': question})

或者A shortcut: get_object_or_404() （官方推荐这个降低代码耦合度  另有get_list_or_404()）
from django.shortcuts import get_object_or_404
question = get_object_or_404(Question, pk=question_id)

##模版代码
The template system uses dot-lookup syntax to access variable attributes. In the example of {{ question.question_text }}, first Django does a dictionary lookup on the object question. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.
Method-calling happens in the {% for %} loop: question.choice_set.all is interpreted as the Python code question.choice_set.all(), which returns an iterable of Choice objects and is suitable for use in the {% for %} tag.
template guide [https://docs.djangoproject.com/en/1.11/topics/templates/]

#移除模板中的hardcoded URLs
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
The way this works is by looking up the URL definition as specified in the polls.urls module. You can see exactly where the URL name of ‘detail’ is defined below:
...
# the 'name' value as called by the {% url %} template tag
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
...
##避免'detail'冲突，添加命名空间
app_name = 'polls'
urlpatterns = ...
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>

#配置atom编辑器
安装插件atom-runner，配置python版本（网上教程有误，缺少scopes）
runner:
  scopes:
    python: "/usr/local/bin/python3.6"

#post
##模版
<h1>{{ question.question_text }}</h1>
{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>

A quick rundown:
The above template displays a radio button for each question choice. The value of each radio button is the associated question choice’s ID. The name of each radio button is "choice". That means, when somebody selects one of the radio buttons and submits the form, it’ll send the POST data choice=# where # is the ID of the selected choice. This is the basic concept of HTML forms.
forloop.counter 循环次数
all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag.
##post数据获取
request.POST['choice']
重定向HttpResponseRedirect(url)

##移除代码中的hardcoded URLs
 return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
 this reverse() call will return a string like '/polls/3/results/'
