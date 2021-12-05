from django.contrib import admin
from .models import Formulario

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display =  ('id', 'id_aluno', 'id_pergunta')

admin.site.register(Formulario, FormAdmin)