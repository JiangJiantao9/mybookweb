#coding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mybook.views.Home', name='home'),
    
    url(r'^serch/', 'mybook.views.Serch_table', name='serch_table'),
    url(r'^books/', 'mybook.views.Serch', name='serch'),
    url(r'^delete/', 'mybook.views.Delete_book', name='delete_book'),
    url(r'^information/', 'mybook.views.Information_serch', name='Information_serch'),
    url(r'^Add_book/', 'mybook.views.Add_book', name='add_book'),
    url(r'^Add_b/', 'mybook.views.add_b', name='add_b'),
    url(r'^Add_author/', 'mybook.views.Add_author', name='add_author'),
    url(r'^Add_a/', 'mybook.views.add_a', name='add_a'),
    url(r'^update/', 'mybook.views.Update_b', name='Update_b'),
    url(r'^update_book/', 'mybook.views.Update_book', name='Update_book'),
    url(r'^admin/', include(admin.site.urls)),
)
