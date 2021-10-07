// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex 04

programa {
	funcao inicio()
	{
	// Declaração de variáveis

	// Vizando facilitar o teste desse algoritmo,
	// O programador pode mudar o 'valor padrão'
	// das Linhas x Colunas dessa matriz,
	
	// atualmente, o valor padrão é 10 (Matriz[10][10])

	// Exemplo: l_c_padrao = 2
	const inteiro l_c_padrao = 10
	inteiro matriz[l_c_padrao][l_c_padrao], l, c
	
	// Entrada dos Valores por parte do usuário
	para(l = 0; l < l_c_padrao; l++){
		para(c = 0; c < l_c_padrao; c++){
			escreva("Digite o valor da posição ", l, "x", c," dessa matriz: ")
			leia(matriz[l][c])
			}
		}

	//Imprime na tela
	escreva("Os elementos, excluindo aqueles da diagonal principal, são: \n")
	para(l = 0; l < l_c_padrao; l++){
		para(c = 0; c < l_c_padrao; c++){
			// Verifica se o laço está passando por um elemento da diagonal principal
			// Exemplo: (0x0, 1x1, 2x2, 3x3...)
			se(l == c){
			escreva("[X]")
				}
			senao{
			escreva("[",matriz[l][c],"]")
				}
			}
			escreva("\n")
		}
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 950; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {matriz, 19, 9, 6}-{l, 19, 41, 1}-{c, 19, 44, 1};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */