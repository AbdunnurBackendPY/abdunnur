from . import views
from django.urls import path, include

from .views import MyDetailView

urlpatterns = [path('', views.index, name='Cat'),
              path('', MyDetailView.as_view(), name='admin'),
              path('accounts/',include('django.contrib.auth.urls'))
]

