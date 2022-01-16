def perguntar():
    return input('\nO que deseja fazer: \n'
                 '<I> - Para Inserir um usuario\n'
                 '<P> - Para Pesquisar um usuario\n'
                 '<E> - Para Excluir um usuario\n'
                 '<L> - Para Listar um usuario: ').upper()

def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                                   input('Digite a última data de acesso: '),
                                                   input('Digite a última estação acessada: ').upper()]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print(f'nome.....: {lista[0]}')
        print(f'último acesso...: {lista[1]}')
        print(f'última estação....: {lista[2]}')

def excluir (dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print('objeto eliminado')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print('objeto....:')
        print(f'login....: {chave}')
        print(f'dados....: {valor}')
