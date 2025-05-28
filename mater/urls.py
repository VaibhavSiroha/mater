"""This in not the main view"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('accounts/', include('accounts.urls')),
#    path('matches/', include('matches.urls')),
#    path('chats/', include('chats.urls')),
]