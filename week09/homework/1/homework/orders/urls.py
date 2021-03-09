from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from orders import views
from rest_framework.documentation import include_docs_urls


# 功能     路径             方式
# 创建用户  /usersapi/      POST
# 查看用户  /users/         GET
# 查看订单  /order/         GET
# 创建订单  /order/         POST



router = DefaultRouter()
router.register(r'orders', views.OrdersViewSet, 'order_list' )
router.register(r'users', views.UserViewSet,  )
router.register(r'usersapi', views.CreateUserViewSet, 'user_api')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
