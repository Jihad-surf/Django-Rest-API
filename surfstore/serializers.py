from rest_framework import serializers
from surfstore.models import Praia, Prancha, Cliente, Compra

class PranchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prancha
        fields = '__all__'
        # exclude = []
    # como o nivel do surfista é um choices, ele fornece a chave e nao o valor, assim se eu quiser ver o valor tenho criar uma nova field    
    nivel_surfista2 = serializers.SerializerMethodField()
    # essa funcao vai pegar essa field acima e vai colocar o objeto nivel_surfista. repare que os nomes sao importantes
    def get_nivel_surfista2(self,obj): # get_<newFieldName>
        return obj.get_nivel_surfista_display() #get_<oldFieldName>_display()
    
    # validação do preço, eu poderia colocar essa validacao diretamente na model, mas as vezes a api precisa de alguma validacao direfente, entao uso o validade<fieldName>
    def validate_preco(self,preco):
        if preco < 0:
            raise serializers.ValidationError("O preço deve ser maior que 0")
        elif preco > 10000:
            raise serializers.ValidationError("O preço deve ser menor que 10.000,00")
        return preco

class PraiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Praia
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade','telefone', 'praia']

class ClienteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cidade','idade','telefone', 'praia']

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class ComprasClienteSerializer(serializers.ModelSerializer):
    # ao invez de mostrar o id do cliente e o id da prancha que o cliente comprou mostra o nome
    cliente = serializers.CharField(source='cliente.nome', read_only=True)
    prancha = serializers.CharField(source='prancha.nome', read_only=True)
    class Meta:
        model = Compra
        fields = '__all__'
