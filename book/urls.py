
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/',meramail),
    path('accounts/', include('accounts.urls')),
    path('', include('books.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

