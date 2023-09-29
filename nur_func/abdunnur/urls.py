from . import views
from django.urls import path



urlpatterns = [path('', views.homepage, name='home'),
               path('cookie/', views.delete_cookies, name='delete')]