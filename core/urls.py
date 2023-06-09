from django.urls import path
from core import views

#Generic
urlpatterns = [
    path('home/', views.index, name='home')
]

#Aluno
urlpatterns += [
    path('listaralunos/', views.listaAlunos.as_view(), name='ListaAlunos'),
    path('cadastraraluno/', views.cadastroAluno, name='CadastroAlunos'),
    path('editaraluno/<int:pk>', views.editarAluno, name='EditarAluno'),
    path('excluiraluno/<int:pk>', views.excluirAluno, name='ExcluirAluno'),
    path('detalhesaluno/<int:pk>', views.detalhesAluno.as_view(), name='DetalhesAluno')
]

#Responsavel
urlpatterns += [
    path('listarresponsavel/', views.listaResponsavel.as_view(), name='ListaResponsavel'),
    path('cadastrarresponsavel/', views.cadastroResponsavel, name='CadastroResponsavel'),
    path('editarresponsavel/<int:pk>', views.editarResponsavel, name='EditarResponsavel'),
    path('excluirresponsavel/<int:pk>', views.excluirResponsavel, name='ExcluirResponsavel'),
    path('detalhesresponsavel/<int:pk>', views.detalhesResponsavel.as_view(), name='DetalhesResponsavel')

]

#Professor
urlpatterns += [
    path('listarprofessor/', views.listaProfessor.as_view(), name='ListaProfessor'),
    path('professor/cadastrarprofessor', views.cadastroProfessor, name='CadastroProfessor'),
    path('editarprofessor/<int:pk>', views.editarProfessor, name='EditarProfessor'),
    path('excluirprofessor/<int:pk>', views.excluirProfessor, name='ExcluirProfessor'),
    path('detalhesprofessor/<int:pk>', views.detalhesProfessor.as_view(), name='DetalhesProfessor')
]

#Valores
urlpatterns += [
    path('listavalores/', views.listaValores.as_view(), name='ListaValores'),
    path('valores/cadastrarvalores', views.cadastroValores, name='CadastroValores'),
    path('editarvalores/<int:pk>', views.editarValores, name='EditarValores'),
    path('excluirvalores/<int:pk>', views.excluirValores, name='ExcluirValores'),
    path('detalhesvalores/<int:pk>', views.detalhesValores.as_view(), name='DetalhesValores')
]

#Financeiro
urlpatterns += [
    path('listacaixas/', views.listaFinanceiro.as_view(), name='ListaFinanceiro'),
    path('abrircaixa/', views.cadastroFinanceiro, name='CadastroFinanceiro'),
    path('detalhescaixa/<int:pk>', views.detalhesFinanceiro.as_view(), name='DetalhesFinanceiro'),
    path('editarfinanceiro/<int:pk>', views.editarFinanceiro, name='EditarFinanceiro'),
    path('excluirfinanceiro/<int:pk>', views.excluirFinanceiro, name='ExcluirFinanceiro')
]

#Chamada
urlpatterns += [
    path('listachamada/', views.listaChamada.as_view(), name='ListaChamada'),
    path('chamada/cadastrarchamada', views.cadastroChamada, name='CadastroChamada'),
    path('detalheschamada/<int:pk>', views.detalhesChamada.as_view(), name='DetalhesChamada'),
    path('editarchamada/<int:pk>', views.detalhesChamada.as_view(), name='EditarChamada'),
    path('excluirchamada/<int:pk>', views.excluirChamada, name='ExcluirChamada')
]

#Ficha
urlpatterns += [
    path('listaficha/', views.listaFicha.as_view(), name='ListaFicha'),
    path('ficha/cadastrarficha', views.cadastroFicha, name='CadastroFicha'),
    path('detalhesficha/<int:pk>', views.detalhesFicha.as_view(), name='DetalhesFicha'),
    path('editarficha/<int:pk>', views.detalhesFicha.as_view(), name='EditarFicha'),
    path('excluirficha/<int:pk>', views.excluirFicha, name='ExcluirFicha')
]