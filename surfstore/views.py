from rest_framework import viewsets, generics, filters
from surfstore.models import Praia,Prancha, Cliente, Compra
from surfstore.serializers import PraiaSerializer,PranchaSerializer, ClienteSerializer, ComprasSerializer,ComprasClienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend

class PranchaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as pranchas"""
    queryset = Prancha.objects.all()
    serializer_class = PranchaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['preco']

class PraiaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as praias"""
    queryset = Praia.objects.all()
    serializer_class = PraiaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ComprasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Clientes"""
    queryset = Compra.objects.all()
    serializer_class = ComprasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ComprasClienteView(generics.ListAPIView):
    """Exibindo todas as pranchas de um cliente"""
    def get_queryset(self):
        queryset = Compra.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ComprasClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
