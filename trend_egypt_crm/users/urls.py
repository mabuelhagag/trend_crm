from django.urls import path, include
from rest_framework import serializers, viewsets, routers

from trend_egypt_crm.users.models import User
from trend_egypt_crm.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'company', 'phone', 'email', 'balance', 'authorization', 'reseller', 'private']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
