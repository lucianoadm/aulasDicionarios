def perguntar():
    return input('\nEscolha uma opção:\n'
                 '<I> - Para Inserir um item\n'
                 '<P> - Para Pesquisar um item\n'
                 '<E> - Para Excluir um item\n'
                 '<R> - Para Resumir um item\n'
                 '<L> - Para Listar os itens: ').upper()

def inserir(inventario):
    inventario[input('Digite o serial: ').upper()] = [input('Digite o material: ').upper(),
                                                   float(input('Digite a quantidade: ')),
                                                   float(input('Digite o Valor unitário: ')),
                                                   input('Digite a natureza do material: ').upper()]

def pesquisar(inventario, chave):
    lista = inventario.get(chave)

    if lista != None:
        print(f'Material.....: {lista[0]}')
        print(f'Natureza.....: {lista[3]}')
        custo_total = lista[1] * lista[2]
        print(f'custo total..: {custo_total}')

def excluir(inventario, chave):
    if inventario.get(chave) != None:
        del inventario[chave]
    print('Objeto eliminado!')

def listar(inventario):
    for chave, valor in inventario.items():
        print('Material....:')
        print(f'Serial....: {chave}')
        print(f'dados.....: {valor}')


