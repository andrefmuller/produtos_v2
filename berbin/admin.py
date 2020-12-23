from django.contrib import admin
from .models import Produto

# Register your models here.
@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto',
                    'preco_venda_produto',
                    'localizacao_produto',
                    'codigo_fabricante_produto',
                    'codigo_ncm_produto',
                    'quantidade_produto',
                    'tipo_volume_produto',
                    )
    search_fields = ('nome_produto','codigo_fabricante_produto')