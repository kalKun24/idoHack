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
        default='infomation'
    )
    title = models.CharField(max_length=50)
    message = models.TextField()
    
    autohr = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field="username")
    
    # 日時
    created_at = models.DateTimeField(auto_now_add=True) #データ挿入時
    updated_at = models.DateTimeField(auto_now=True) #データ更新時
    
    def __str__(self):
        return self.title