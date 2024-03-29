"""
URL configuration for {{ project_name }} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Apps.
    path(route='', view=include('base.urls')),
    path(route='accounts/', view=include('accounts.urls')),
    # Django.
    path(route='accounts/', view=include('django.contrib.auth.urls')),
    path(route='admin/', view=admin.site.urls),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path(route='rosetta/', view=include('rosetta.urls'))
    ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path(route='__debug__/', view=include(debug_toolbar.urls)),
    )
    urlpatterns += static(
        prefix=settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
