from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('leadsapi.urls')),
    path('', include('accounts.urls'))
]
