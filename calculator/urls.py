from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^calcu/$', 'calculator.cal.views.calcu',name='calcu'),
   
)
