"""
URL configuration for app_server project.

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
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from user import urls as auth_urls
from user.views import UserDetailAPI
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include(auth_urls)),
    path("api/v1/user/<int:id>", UserDetailAPI.as_view()),
    path('', views.index)

]

handler404 = views.handler404
handler500 = views.handler500

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
