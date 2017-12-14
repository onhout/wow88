from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.salesperson_index, name='salesperson_index'),
    url(r'^signup/$', views.salesperson_signup, name='salesperson_signup')
]
