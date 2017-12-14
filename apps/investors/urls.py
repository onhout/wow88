from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.investors_index, name='investors_index'),
    url(r'^signup/$', views.investors_signup, name='investors_signup')
]
