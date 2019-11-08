from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from search import views

from users import views as user_views

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # User authentication
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Navigation
    # home page
    path('', include('storePage.urls')),
    # user profile setting page which will include security, user information, and billing
    path('settings/', include('users.urls', namespace='settings')),

    #Search page
    path('search/', include('search.urls', namespace='search')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
