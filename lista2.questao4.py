ALGORITMO
" média aritmética"
DECLARE nota1, nota2, nota3, media NÚMERICO

ESCREVA "Digite a primeira nota: "
LEIA nota1

ESCREVA "Digite a segunda nota: "
LEIA nota2

ESCREVA "Digite a terceira nota: "
LEIA nota3

media ← (nota1 + nota2 + nota3) / 3
ESCREVA "Média aritmética: ", media

SE media >= 0 e media < 4
    ENTÃO ESCREVA "Reprovado"

SE media >= 4 e media < 7
    ENTÃO ESCREVA " Prova final"

SE MEDIA >= 7
    ENTAO ESCREVA "Aprovado"

FIM_ALGORITMO
