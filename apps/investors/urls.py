from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.investors_index, name='investors_index'),
    url(r'^signup/$', views.investors_signup, name='investors_signup'),
    url(r'^verify/$', views.investor_verify, name='investors_verify'),
    url(r'^contract/add/$', views.contract_form, name='add_new_contract'),
    url(r'^contract/edit/$', views.edit_contract, name='edit_contracts')
]
