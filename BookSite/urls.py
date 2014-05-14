from django.conf.urls import patterns, include, url

from django.contrib import admin
from App import views
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'file/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.FILE_PATH}),
    url(r'css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),
    url(r'js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
    url(r'img/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.IMG_PATH}),
    url(r'media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'accounts/register/$',views.register),
    url(r'^$',views.home),
    url(r'^search/$',views.search),
    url(r'^category/$',views.category),
    url(r'^myinfo/$',views.myinfo),
    url(r'^comment/$',views.comment),
    url(r'Book/(?P<isbn>.*)$',views.Book),
    url(r'Writer/(?P<id>.*)',views.Writer),
    url(r'Press/(?P<id>.*)',views.Press),
    url(r'Tag/(?P<name>.*)',views.Tag),
    url(r'updateScore',views.update_score),
)
