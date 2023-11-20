from django.db import models

class Prancha(models.Model):
    NIVEL_SURFISTA = (
        ('A', 'Iniciante'),
        ('B', 'Intermediario'),
        ('C', 'Avançado')
    )
    nome = models.CharField(max_length=30)
    preco = models.FloatField()
    nivel_surfista = models.CharField(max_length=1,choices=NIVEL_SURFISTA)

    def __str__(self):
        return self.nome
    
class Praia(models.Model):
    TIPO_ONDA = (
        ('A', 'Cavada'),
        ('B', 'Cheia')
    )
    nome = models.CharField(max_length=30)
    distancia_sp = models.IntegerField()
    tipo_onda = models.CharField(max_length=1,choices=TIPO_ONDA)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20, default='0000000')
    praia = models.ForeignKey(Praia, on_delete=models.DO_NOTHING)

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    prancha = models.ForeignKey(Prancha, on_delete=models.DO_NOTHING)
    data_compra = models.DateField()
 