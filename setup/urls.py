from django.contrib import admin
from django.urls import path, include
from rotas.views import AmbienteViewSet, RotaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ambientes', AmbienteViewSet, basename = 'Ambientes')
router.register('rotas', RotaViewSet, basename = 'Rotas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
