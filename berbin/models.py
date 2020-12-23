from django.db import models
from django.utils import timezone

# Create your models here.

class Produto(models.Model):
    id_produto = models.CharField(max_length=10,blank=True)
    nome_produto = models.CharField(max_length=255)
    codigo_fabricante_produto = models.CharField(max_length=50, blank=True)
    descricao_produto = models.TextField(max_length=500, blank=True)
    codigo_ean_produto = models.CharField(max_length=13,blank=True)
    codigo_ncm_produto = models.CharField(max_length=20,blank=True,null=True )
    preco_venda_produto = models.DecimalField(max_digits=10,
                                              decimal_places=2,
                                              blank=True)
    preco_compra_produto = models.FloatField(max_length=10, blank=False)
    quantidade_produto = models.FloatField(max_length=10,blank=True)
    TIPOVOLUME = (
        ('UNIDADE','UNIDADE'),
        ('GRAMA','GRAMA'),
        ('PACOTE','PACOTE'),
        ('PAR','PAR'),
        ('CONJUNTO','CONJUNTO'),
        ('ML','ML'),
        ('KILOGRAMA','KILOGRAMA'),
        ('TONELADA','TONELADA'),
        ('LITRO','LITRO'),
         ('CAIXA','CAIXA'),
        ('SACO','SACO'),
        ('LATA','LATA'),
        ('KIT','KIT'),
        ('DÚZIA','DÚZIA'),
        ('DEZENA','DEZENA'),
        ('CENTENA','CENTENA'),
        ('MILHAR','MILHAR'),
        ('FARDO','FARDO'))
    tipo_volume_produto = models.CharField(max_length=20,
                                           choices=TIPOVOLUME,
                                           default=None)
    conteudo_produto = models.CharField(max_length=25, blank=True)
    cor_produto = models.CharField(max_length=50, blank=True)
    referencia_produto = models.CharField(max_length=250, blank=True)
    localizacao_produto = models.CharField(max_length=100,blank=True)
    observacao_produto = models.TextField(max_length=500, blank=True)
    data_cadastro_produto = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_produto