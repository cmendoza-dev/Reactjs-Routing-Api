from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-productos/', include('rest_framework.urls', namespace='rest_framework')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
