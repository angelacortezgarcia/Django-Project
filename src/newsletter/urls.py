from django.conf.urls import url
from django.contrib import admin
from newsletter.views import post_create
from newsletter.views import post_list
from newsletter.views import post_detail
from newsletter.views import post_update
from newsletter.views import post_delete
# from newsletter.views import post_list2
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_articles,

)
# from . import views
urlpatterns = [

    url(r'^$', post_list, name='list'), #eto ung gumagana
    url(r'^articles/$', post_articles, name='articles'),
    url(r'^create/$', post_create),
    # url(r'^detail/(?P<id>\d+)/$', post_detail),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),

]
