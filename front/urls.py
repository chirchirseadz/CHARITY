from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_page'),
    path('email_sent_successfull', views.email_sent_successfull, name='email_sent_successfull')
]

