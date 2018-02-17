from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^user_next_step/$', views.user_next_step, name='user_next_step'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^home/$', views.user_home, name='user_home'),
    url(r'^profile/change_password/$', views.account_settings_password, name='user_settings_password'),
]
