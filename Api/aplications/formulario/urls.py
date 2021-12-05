from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("Formulario", views.FormularioApi)
router.register("Aluno", views.AlunoApi)
router.register("Pergunta", views.PerguntaApi)
router.register("Satisfacao", views.SatisfacaoApi)
router.register("Importancia", views.ImportanciaApi)
router.register("Envio", views.EnvioApi)
router.register("Forms", views.QtdFormularios)

urlpatterns = [
    path('', include(router.urls))
]