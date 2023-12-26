from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Infomation(models.Model):
    category = models.CharField(
        max_length=30,
        choices = (
            ('update', 'アップデート'),
            ('infomation', 'お知らせ'),
            ('competition', '競技情報'),
            ('maintenance', 'メンテナンス')
        ),
        default='infomation',
        verbose_name="カテゴリ"
    )
    title = models.CharField(max_length=50, verbose_name="タイトル")
    message = models.TextField(verbose_name="お知らせ内容")
    
    autohr = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field="username", verbose_name="投稿者")
    
    # 日時
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時") #データ挿入時
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時") #データ更新時
    
    def __str__(self):
        return self.title
