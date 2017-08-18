from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from DjangoUeditor.DjangoUeditor.models import UEditorField

# Create your models here.
class BlogsPost(models.Model):
    #添加创建者
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts",to_field="id")
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150,default = "empty subtitle")
    body = UEditorField(
            u'内容	',
            width=600,
            height=300,
            toolbars="full",
            imagePath='upload/image/%(year)s/%(month)s/%(day)s/%(time)s_%(rnd)s.%(extname)s',
            filePath='upload/file/%(year)s/%(month)s/%(day)s/%(time)s_%(rnd)s.%(extname)s',
            upload_settings={"imageMaxSize":10485760},
            settings={},command=None,
            #event_handler=myEventHander(),
            blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    #{'year', 'month', 'day', 'date', 'time', 'datetime', 'rnd', 'basename': 'WechatIMG9', 'extname': 'jpeg', 'filename': 'WechatIMG9.jpeg'}
