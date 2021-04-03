"""hmobiweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [

    # REST FRAMEWORK
    path('api/auth/', include('apps.users.api.urls', namespace='users_api')),
    path('api/ms/', include('apps.monitoring_solutions.api.urls',
                            namespace='monitoring_solutions_api')),
    path('api/us/', include('apps.user_monitoring.api.urls',
                            namespace='user_monitoring_api')),

]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
    openapi.Info(
            title="Health-Moni API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.example.local.com/policies/terms/",
            contact=openapi.Contact(email="example@example.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

