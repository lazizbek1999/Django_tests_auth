from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView
urlpatterns = [
    path("", TemplateView.as_view(template_name="registration/home.html"), name="home"),
    path('signup/', SignUpView.as_view(), name='signup'),
    
]