

from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny 


security_scheme = {
    'BearerAuth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'JWT Authorization header using the Bearer scheme.'
    }
}



schema_view = get_schema_view(
   openapi.Info(
      title="Assignment Full Stack",
      default_version='v1',
      description="API documentation for the assignment app",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=[AllowAny],  

)

# Add your URLs
urlpatterns = [
    # Swagger and Redoc URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'), 
]
