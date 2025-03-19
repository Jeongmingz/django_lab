"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView, \
    SpectacularJSONAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
#     Django REST Framework Spectacular
    path('docs/json/', SpectacularJSONAPIView.as_view(), name='schema-json'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/user', SpectacularAPIView.as_view(), name='user_schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(), name = 'swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(), name='redoc')
]
