# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("base.urls")),
    path('campusVisit/', include("campusVisit.urls")),
    path('scholarship/', include("scholarship.urls")),  # Add this line to include the scholarship URLs
    path('arcAdmin8879/', admin.site.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

admin.site.index_title = "BITS Alumni Relations"
admin.site.site_header = "Alumni Control Admin"
admin.site.site_title = "Alumni Control Admin"

handler404 = 'base.views.handeling_404'
