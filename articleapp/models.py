from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)    # 1:多 연결
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)    # DB 자체적으로 넣어줘라
