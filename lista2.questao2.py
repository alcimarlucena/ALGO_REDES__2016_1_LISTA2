ALGORITMO "Qualidade dos filmes "
DECLARE contador_regular, contador_bom, contador_otimo, opniao INTEIRO

contador_regular ← 0
contador_bom ← 0
contador_otimo ← 0

PARA i de 0 ate 10 faça

ESCREVA "Dê sua opnião em relação a qualidade dos filmes: opção 1 para regular, opção 2 para bom e opção 3 para ótimo: "
LEIA opniao

SE opiniao = 1
	ENTÃO contador_regular ← contador_regular + 1

SE opiniao = 2
	ENTÃO contador_bom ← contador_bom + 1

SE opiniao = 3
	ENTÃO contador_otimo ← contador_otimo + 1

SENÃO
	ESCREVA "opção invalida!"

ESCREVA "A quantidade de pessoas que responderam regular é: ",contador_regular
ESCREVA "A quantidade de pessoas que responderam bom é: ",contador_bom
ESCREVA "A quantidade de pessoas que responderam otimo é: ",contador_otimo

FIM_ALGORITMO