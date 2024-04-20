"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="To Do API",
      default_version='v1',
      description="TO Do description",
      terms_of_service="https://127.0.0.1:8000/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name = 'schema-swagger-ui'),
    path('api/todo/',include('todoapi.urls')),
    # path('api/book/' ,include('book.urls')),
    path('api/token/',swagger_auto_schema(method='post',security=[]) (TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/token/refresh/',swagger_auto_schema(method='post',security=[]) (TokenRefreshView.as_view()), name='token_refresh'),
    path('api/user/',include('user.urls')),
]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT,)
