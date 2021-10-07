// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex.03 "Programa Multiplicação de Matrizes"

// Obs:
// Não é possível Multiplicar matrizes na ordem AxB,
// Se Y for diferente de W, dada matrizes A(X,Y) e B(W,Z) 

programa {
	funcao inicio() {
		// Declaração de variáveis
		inteiro l_aux, c_aux, l = 0, c = 0, contador
		real A[100][100], B[100][100], MULTI[100][100], 
		multi_aux = 0.0

		// Entrada dos Valores por parte do usuário
		escreva("Insira o número de linhas das matrizes (Mín: 1 - Máximo 100): ")
		leia(l_aux)
		escreva("Insira o número de colunas das matrizes (Mín: 1 - Máximo 100): ")
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

		// Faz o cálculo da Matriz 'Multiplicação'
		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				multi_aux = 0.0
				para(contador = 0; contador < c_aux; contador++){
					multi_aux = multi_aux + (A[l][contador] * B[contador][c])
					}
				MULTI[l][c] = multi_aux
			}
		}

		// Imprime a Matriz Multiplicação
		escreva("Matriz 'Multiplicação' = A x B: \n")
		para (l = 0; l < l_aux ; l++)
		{
			para (c = 0 ; c < c_aux ; c++)
			{
				escreva("[",MULTI[l][c],"]")
				
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
 * @POSICAO-CURSOR = 647; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {l, 13, 24, 1}-{c, 13, 31, 1}-{A, 14, 7, 1}-{B, 14, 20, 1}-{MULTI, 14, 33, 5}-{multi_aux, 15, 2, 9};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */