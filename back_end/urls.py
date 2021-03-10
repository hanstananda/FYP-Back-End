"""back_end URL Configuration

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
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

from back_end import settings
from classifier.views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snake_info', SnakeInfoViewSet)
router.register(r'snake_image', SnakeImageViewSet)
router.register(r'snake_classification', ClassifySnakeRequestViewSet)
router.register(r'expert_classification', ExpertClassificationViewSet)
router.register(r'random_snake_image', SnakeImageRandomViewSet)
router.register(r'snake_list', SnakeInfoReadOnlyViewSet)
router.register(r'snake_report', SnakeReportViewSet)
router.register(r'snake_report_view', SnakeReportReadOnlyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
