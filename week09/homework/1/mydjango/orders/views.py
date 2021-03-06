from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from .serializers import CreateUserSerializer, UserSerializer, OrdersSerializer
from rest_framework.decorators import api_view
from rest_framework import filters
from django_filters import rest_framework as rf_filters
from rest_framework import serializers
from order.models import Orders
from .serializers import OrdersSerializer

from notifications.signals import notify
from django.forms.models import model_to_dict

class CreateUserViewSet(viewsets.ModelViewSet):
    """
    创建用户视图
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        """ 
        创建用户 
        """
        serializer = CreateUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

# class ProfileAPIViewSet(viewsets.ModelViewSet):
#     """
#     用户积分
#     """
    
#     queryset = ProfileAPI.objects.all()
#     serializer_class = ProfileAPISerializer
    

class OrdersViewSet(viewsets.ModelViewSet):
    """
    订单视图
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def retrieve(self, request, pk=None):
        """ order详情 """
        # 获取实例
        user = self.get_object()
        # 序列化
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @api_view(['POST'])
    def create(self, request, *args, **kwargs):
        """
        创建order
        """
        serializer = OrdersSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    查看用户视图
    """
    # url = serializers.HyperlinkedIdentityField(view_name="myapp:user-detail")
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        serializer = self.get_serializer(user)
        data = serializer.data

        # 接收通知
        user_notify = User.objects.get(pk=user.pk)
        # notify_dict = model_to_dict(user_notify.notifications.unread().first(), fields=["verb",])
        
        new_dict= {}
        for obj in user_notify.notifications.unread():
            notify_dict = model_to_dict(obj, fields=["verb",])
            new_dict.setdefault("verb", []).append(notify_dict["verb"])
            # dict(data, **notify_dict)
        
        return Response(dict(data, **new_dict))


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_detail', request=request, format=format),
        'userapi': reverse('user_api', request=request, format=format),
        'orders': reverse('order_list', request=request, format=format),
    })


