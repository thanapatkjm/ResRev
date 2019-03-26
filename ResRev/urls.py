from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='ResRev'
urlpatterns = [
    path('', TemplateView.as_view(template_name="FrontPage.html"), name='home'),
    path('regist/', TemplateView.as_view(template_name="Register.html") , name='regist'),
    path('new_rest/', TemplateView.as_view(template_name="new_rest.html") , name='new_rest'),
    path('registering/', views.registering , name='registering'),
]
