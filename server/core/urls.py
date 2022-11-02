
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from category.views import CategroryView
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()
# router.register(r'blogs', BlogView)
router.register(r'categories', CategroryView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/blog/', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
