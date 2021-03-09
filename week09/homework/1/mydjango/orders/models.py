from django.db import models

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Orders(models.Model):
    '''
    订单
    '''
    __tablename__ = 'orders'
    order_id = models.AutoField(primary_key=True)   # id
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    order_describe = models.CharField(max_length=30, verbose_name='订单描述', default='')
    order_creater = models.ForeignKey(
        'auth.User', verbose_name='用户id', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['create_time']    

    def __str__(self):
        return self.order_describe
