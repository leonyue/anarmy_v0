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
