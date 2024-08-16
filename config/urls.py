from django.contrib import admin
from django.urls import path, include
from pages.views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page URL
    path('about/', AboutPageView.as_view(), name='about'),  # About page URL
    path('admin/', admin.site.urls),  # Admin site
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
    path('accounts/', include('accounts.urls')),  # Custom account URLs
    path('posts/', include('posts.urls')),  # Include the posts app URLs
]
