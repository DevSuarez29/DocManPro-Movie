"""
URL configuration for docmanpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.FrontEnd.home import *
from app.api import urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', home, name='home'),
    path('movie/<movie_id>/', movie_detail, name='movie_detail'),
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('docs/', include_docs_urls(title='Documentacion API')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
