"""gestimunus URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gestimunus import settings
from django.conf.urls.static import static

from tools import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'', admin.site.urls),
    url(r'^export_action/', include("export_action.urls", namespace="export_action")),
    url(r'^eventjson/', views.eventsFeed),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^uploads/', views.(...)),
    # url(r'^adminlte/', include('adminlte.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', include({"document_root": settings.STATIC_ROOT})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG==False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
