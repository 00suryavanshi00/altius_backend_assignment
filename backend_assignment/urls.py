
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('documentation/v1/', include('app_documentation.urls')),
    path('assignment/v1/', include('alt_assignment.urls')),
    path('', RedirectView.as_view(url='documentation/v1/swagger/', permanent=True)),

]
