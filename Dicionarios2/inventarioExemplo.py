from Dicionarios2.funcao import *
materiais = {}

opcao = perguntar()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(materiais)
    if opcao == 'P':
        pesquisar(materiais, input('Qual material deseja pequisar? '))
    if opcao == 'E':
        excluir(materiais, input('Qual material deseja excluir: '))
    if opcao == 'L':
        listar(materiais)
    opcao = perguntar()


