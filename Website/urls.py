"""
Definition of urls for E_COMMERCE.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('brands/', views.brands, name='brands'),
    
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),


    path('register/',
         LoginView.as_view
         (
             template_name='app/register.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Create Account',
                 'year' : datetime.now().year,
             }
         ),
         name='register'),
    path('register/', LogoutView.as_view(next_page='/'), name='register'),

    path('cart/',
         LoginView.as_view
         (
             template_name='app/cart.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Payment',
                 'year' : datetime.now().year,
             }
         ),
         name='cart'),
    path('cart/', LogoutView.as_view(next_page='/'), name='cart'),
    
]
