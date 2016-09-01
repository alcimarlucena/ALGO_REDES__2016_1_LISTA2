''' algoritmo de média aritmética e a mensagem de reprovado ou aprovado ou prova final '''
nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 +nota3) / 3

if media >=7:
    print(nome,'parabéns,sua média é %.2f e você está Aprovado.' %(media))
elif media >=4 and media <7:
    print(nome,'sua média é %.2f e você vai ter que fazer Prova Final.' %(media))
else:
    print(nome,'infelizmente sua média é %.2f, você está Reprovado.'%(media))
