from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("services/", include("apps.services.urls")),
    path("quotes/", include("apps.quotes.urls")),
    path("gallery/", include("apps.gallery.urls")),
    path("education/", include("apps.education.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
