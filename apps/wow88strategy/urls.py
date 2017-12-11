from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^contact_us_message$', views.contact_us_message, name='contact_us_message'),
]
