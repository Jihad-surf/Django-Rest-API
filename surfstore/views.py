from rest_framework import viewsets, generics, filters
from surfstore.models import Praia,Prancha, Cliente, Compra
from surfstore.serializers import PraiaSerializer,PranchaSerializer, ClienteSerializer, ComprasSerializer,ComprasClienteSerializer, ClienteSerializerV2
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend

class PranchaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as pranchas"""
    # dados a serem exibidos
    queryset = Prancha.objects.all()
    # transforma a model em json
    serializer_class = PranchaSerializer
    # nao fica publica, para ter acesso precisa fazer login
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # configura os filtros e ordenação
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # passa os Field que podem ser ordenado
    ordering_fields = ['preco']
    # passa os Field que podem ser filtrado
    filterset_fields = ['nome', 'nivel_surfista', 'preco']

class PraiaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as praias"""
    queryset = Praia.objects.all()
    serializer_class = PraiaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Clientes"""
    queryset = Cliente.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ClienteSerializerV2
        else:
            return ClienteSerializer

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
