// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex.05 "Soma De matrizes 4x4"

programa {
	funcao inicio() {
		
		// Declaração de variáveis

		// Vizando facilitar o teste desse algoritmo,
		// O programador pode mudar o valor padrão
		// das Linhas x Colunas dessa matriz, atualmente 4 (Matriz[4][4])
		const inteiro l_c_padrao = 4
		
		real A[l_c_padrao][l_c_padrao], 
		B[l_c_padrao][l_c_padrao], 
		SOMA[l_c_padrao][l_c_padrao]

		inteiro l_aux, c_aux, l = 0, c = 0

		// Entrada dos Valores por parte do usuário

		para (l = 0; l < l_c_padrao ; l++)
		{
			para (c = 0 ; c < l_c_padrao ; c++)
			{
				escreva("Informe o elemento ",l,"x", c," da matriz A: ")
				leia(A[l][c])
			}
		}
		
		para (l = 0; l < l_c_padrao ; l++)
		{
			para (c = 0 ; c < l_c_padrao ; c++)
			{
				escreva("Informe o elemento ",l,"x",c," da Segunda matriz: ")
				leia(B[l][c])
			}
		}
			
		// Imprime na tela as matrizes A e B, respectivamente	
		escreva("Matriz A: \n")
		para (l = 0; l < l_c_padrao ; l++)
		{
			para (c = 0 ; c < l_c_padrao ; c++)
			{
				escreva(A[l][c]," , ")
			}
			escreva("\n")
		}
		
		escreva("Matriz B: \n")
		para (l = 0; l < l_c_padrao ; l++)
		{
			para (c = 0 ; c < l_c_padrao ; c++)
			{
				escreva(B[l][c]," , ")
			}
			escreva("\n")
		}

		// Cálcula e Imprime a Matriz 'SOMA'
		escreva("Matriz 'Soma' = A + B: \n")

		para (l = 0; l < l_c_padrao ; l++)
		{
			para (c = 0 ; c < l_c_padrao ; c++)
			{
				SOMA[l][c] = A[l][c] + B[l][c]
				escreva(SOMA[l][c]," , ")
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
 * @POSICAO-CURSOR = 80; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {A, 16, 7, 1}-{B, 17, 2, 1}-{SOMA, 18, 2, 4};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */