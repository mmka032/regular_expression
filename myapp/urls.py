from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('regex_app/', include('regex_app.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/regex_app/')),
]
