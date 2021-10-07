// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex.02 "Programa Soma de Matrizes"

// Obs:
// Não é possível somar ou subtrair matrizes de ordem diferente 

programa {
	funcao inicio() {
		// Declaração de variáveis
		inteiro l_aux, c_aux, l = 0, c = 0
		real A[100][100], B[100][100], SOMA[100][100]

		// Entrada dos Valores por parte do usuário
		escreva("Insira o número de linhas das matrizes: ")
		leia(l_aux)
		escreva("Insira o número de colunas das matrizes: ")
		leia(c_aux)		
		
		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				escreva("Informe o elemento ",l,"x", c," da matriz A: ")
				leia(A[l][c])
			}
		}
		
		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				escreva("Informe o elemento ",l,"x",c," da Segunda matriz: ")
				leia(B[l][c])
			}
		}
			
		// Imprime na tela		
		escreva("Matriz A: \n")
		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				escreva("[",A[l][c],"]")
			}
			escreva("\n")
		}
		
		escreva("Matriz B: \n")
		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				escreva("[",B[l][c],"]")
			}
			escreva("\n")
		}

		escreva("Matriz 'Soma' = A + B: \n")

		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				SOMA[l][c] = A[l][c] + B[l][c]
				escreva("[",SOMA[l][c],"]")
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
 * @POSICAO-CURSOR = 1397; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {A, 13, 7, 1}-{B, 13, 20, 1}-{SOMA, 13, 33, 4};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */