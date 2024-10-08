from django.contrib import admin
from django.urls import path, include
from pages.views import HomePageView, AboutPageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page URL
    path('about/', AboutPageView.as_view(), name='about'),  # About page URL
    path('admin/', admin.site.urls),  # Admin site
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
    path('accounts/', include('accounts.urls')),  # Custom account URLs
    path('posts/', include('posts.urls')),  # Include the posts app URLs
    
    # Password change URLs
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url='/accounts/password_change/done/'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Password reset URLs
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
