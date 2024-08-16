from django.contrib import admin
from django.urls import path, include
from pages.views import HomePageView, AboutPageView
from django.contrib.auth import urls

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
