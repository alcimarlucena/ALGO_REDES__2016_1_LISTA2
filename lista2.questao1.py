'''
AVALIAR A QUALIDADE DOS FILMES
'''
#Contadores
contador_regular = 0
contador_bom = 0
contador_ótimo = 0

for i in range(10):
    opniao = int(input('Dê sua opnião em relação a qualidade dos filmes: opção 1 para regular, opção 2 para bom e opção 3 para ótimo: '))

    if opniao == 1:
        contador_regular = contador_regular + 1
        print('regular')
    elif opniao == 2:
        contador_bom = contador_bom + 1
        print('bom')
    elif opniao == 3:
        contador_ótimo = contador_ótimo + 1
        print('ótimo')
    else:
        print('Opção inválida!')
#Apresentação dos quantitativos
print('a) %d pessoa(s) respondeu(ram) ótimo.' %contador_ótimo)
print('b) %d pessoa(s) respondeu(ram) bom.' %contador_bom)
print('c) %d pessoa(s) respondeu(ram) regular.' %contador_regular)