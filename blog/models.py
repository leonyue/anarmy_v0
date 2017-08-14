from django.db import models
from django.utils import timezone
from DjangoUeditor.DjangoUeditor.models import UEditorField

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150,default = "empty subtitle")
    body = UEditorField(
            u'内容	',
            width=600,
            height=300,
            toolbars="full",
            imagePath="",
            filePath="",
            upload_settings={"imageMaxSize":1204000},
            settings={},command=None,
            #event_handler=myEventHander(),
            blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
