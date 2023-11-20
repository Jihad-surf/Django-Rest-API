from django.contrib import admin
from django.urls import path, include
from surfstore.views import PraiaViewSet,PranchaViewSet, ClienteViewSet, ComprasViewSet, ComprasClienteView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('praias', PraiaViewSet, basename='Praias')
router.register('pranchas', PranchaViewSet, basename='Pranchas')
router.register('clientes', ClienteViewSet, basename='Clientes')
router.register('compras', ComprasViewSet, basename='Compras')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('clientes/<int:pk>/compras/', ComprasClienteView.as_view())
]
