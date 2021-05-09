from django.db import models

# Create your models here.

# １つのクラスが１つのテーブルと紐づく
class Post(models.Model):
    # CharField -> 固定長の文字列
    title = models.CharField(
        'タイトル', max_length=100
    )
    # TextField -> 自由長の文字列
    body = models.TextField('本文')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)