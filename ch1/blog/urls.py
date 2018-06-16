from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category_list, name="category_list"),
    url(r'^new/$', views.post_new, name="post_new"),
    url(r'^(?P<name>\w+)/$', views.post_list, name="post_list"),
    url(r'^(?P<name>\w+)/(?P<id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^(?P<name>\w+)/(?P<id>\d+)/edit/$', views.post_edit, name="post_edit"),

]