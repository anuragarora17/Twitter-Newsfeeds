from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from newsfeeds.models import News
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['tag', 'heading', 'body', 'time', 'link']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [url(r'^$', include('newsfeeds.urls')),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^news/', include('newsfeeds.urls')),
               url(r'^api-auth/', include('rest_framework.urls',
                                          namespace='rest_framework'))]
