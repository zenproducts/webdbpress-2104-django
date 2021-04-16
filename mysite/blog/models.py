from django.db import models


class Post(models.Model):
    title = models.CharField("タイトル", max_length=100)
    body = models.TextField("本文")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
