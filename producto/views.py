from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.static import serve

# Create your views here.
# ViewSets define the view behavior.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    parser_classes = (MultiPartParser, FormParser)

def serve_image(request, path):
    # Ruta al directorio de imágenes en tu proyecto
    image_directory = 'media/productos/'
    return serve(request, path, document_root=image_directory)


