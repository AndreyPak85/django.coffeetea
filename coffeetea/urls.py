"""coffeetea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from start import views as viewshome
from authapp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin-secure/', admin.site.urls),
    url(r'^$', viewshome.home, name='home' ),
    url(r'^authapp/$', views.auth, name='auth' ),

    url(r'^authapp/login/$', auth_views.login,
        {'template_name': 'login.html'},
        name='authapp-login' ),

    url(r'^authapp/logout/$', auth_views.logout,
        {'next_page': '/authapp/'},
        name='authapp-logout' ),

    url(r'^coffee/(?P<coffee_id>\d+)$', viewshome.coffee, name='coffee_detail'),

    url(r'^authapp/sign-up', views.authapp_sign_up, name='authapp-sign-up'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
