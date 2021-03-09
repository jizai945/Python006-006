# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from .models import Orders
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view


# class ProfileAPISerializer(serializers.HyperlinkedModelSerializer):
#     """用户积分序列"""
#     lookup_field = 'id'
#     class Meta:
#         model = ProfileAPI
#         fields = ['url','score', 'owner']
#     extra_kwargs = {
#         'url': {'lookup_field': 'id'},
#         'owner': {'lookup_field': 'id'}
#         }

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Orders
        fields = ['order_id', 'create_time', 'order_describe', 'order_creater']

    @api_view(['GET'])
    def showdata(request):
        id = request.GET['order_id']
        datas=Posts.objects.filter(order_id=id)
        postdata = PostsSerializer(datas,many=True)
        return Response({'data':PostsSerializer.data})

    @api_view(['POST'])
    def create_data(self, request):
        id = request.GET['order_id']
        datas = Orders.objects.filter(order_id=id)
        order_data = OrdersSerializer(datas, many=True)
        return Response({'order_data': OrdersSerializer.data})


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    """创建用户序列"""

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', ]
    
    def validate(self, attrs):
 		# 对密码进行加密 
        attrs['password'] = make_password(attrs['password'])
        return attrs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户序列"""
    # articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())
    # articles = ArticlesSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', ]



