// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 1) Desenvolver um algoritmo que:

// Receba os valores de uma matriz de 4 linhas e 4 colunas
// E mostre quais são os elementos da diagonal principal

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro matriz[4][4], l, c
	
	// Entrada dos Valores por parte do usuário
	escreva("Identificador dos elementos da diagonal principal de uma matriz 4x4 \n")

	para(l = 0; l < 4; l++){
		para(c = 0; c < 4; c++){
			escreva("Digite o valor da posição ", l, "x", c," dessa matriz: ")
			leia(matriz[l][c])
			}
		}

	//Imprime na tela
	escreva("Os elementos da diagonal principal são, respectivamentes: \n")
	para(l = 0; l < 4; l++){
		para(c = 0; c < 4; c++){
			// Verifica se o loop está passando por um elemento da diagonal principal
			// Exemplo: (0x0, 1x1, 2x2, 3x3)
			se(l == c){
				escreva("[",matriz[l][c],"]")
				}
			}
		}
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 907; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {matriz, 15, 9, 6}-{l, 15, 23, 1}-{c, 15, 26, 1};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */