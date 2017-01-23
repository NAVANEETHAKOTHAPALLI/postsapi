from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
from posts.views import PostViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

post_highlight = PostViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url('^schema/$', schema_view),
    ...
]

urlpatterns = format_suffix_patterns([
	url(r'^$', api_root),
    url(r'^posts/$',post_list, name ='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', post_detail, name = 'post-detail'),
    url(r'^posts/(?P<pk>[0-9]+)/highlight/$', post_highlight, name = 'post-highlight'),
    url(r'^users/$', user_list, name = 'user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name = 'user-detail'),
])

urlpatterns += [
     url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)