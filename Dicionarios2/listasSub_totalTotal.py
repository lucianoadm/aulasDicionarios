inventario = []
resposta = 'C'
while resposta == 'C':
    materiais = [input('Digite o material: ').upper(),
                 int(input('Digite a quantidade: ')),
                 float(input('Digite o Valor unitário: '))]
    inventario.append(materiais)
    resposta = input('Digite \'C\' para continuar \'S\' para sair: ').upper()

sub_total = 0
total = 0
for i in inventario:
    sub_total = i[1] * i[2]
    print(f'subtotal....:{sub_total}')
    total += sub_total
print(total)
