from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^', view=views.atm_login, name='ATMLogin'),
]
