from django.db import models

from ..aluno.models import Aluno
from ..satisfacao.models import Satisfacao
from ..importancia.models import Importancia
from ..pergunta.models import Perguntas
from ..envio.models import Envio

class Formulario(models.Model):
    # id=models.IntegerField(primary_key=True, auto_created=True, default=0)
    id_aluno = models.ForeignKey(Aluno, related_name="fk_aluno", on_delete=models.CASCADE)
    id_pergunta = models.ForeignKey(Perguntas, related_name="fk_pergunta", on_delete=models.CASCADE)
    id_satisfacao = models.ForeignKey(Satisfacao, related_name="fk_satisfacao", on_delete=models.CASCADE)
    id_importancia = models.ForeignKey(Importancia, related_name="fk_importancia", on_delete=models.CASCADE)
    semestre = models.ForeignKey(Envio, related_name="fk_envio", on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500, default="", blank=True)
    
      
    def __str__(self):
        return '%s' % self.id_aluno