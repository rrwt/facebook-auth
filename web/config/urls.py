from django.contrib import admin
from django.urls import path, include

from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_views.HomePage.as_view(), name='home_page')
]
