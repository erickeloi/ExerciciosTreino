// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex.08 "Programa Multiplicação de Matrizes" 	

programa {
	funcao inicio() {
		// Declaração de variáveis
		inteiro C,D,E,F,
		l = 0, c = 0, contador
		
		real A[6][6], B[6][6], MULTI[6][6],
		multi_aux = 0.0

		// Entrada dos Valores por parte do usuário
		escreva("Insira o número de linhas da Matriz A: ")
		leia(C)
		enquanto(C < 1 ou C > 6) {
			escreva("Digite um Resultado Válido, menor que 7 e maior que 0: ")
			leia(C)
			}
		escreva("Insira o número de colunas da Matriz A: ")
		leia(D)
		enquanto(D < 1 ou D > 6) {
			escreva("Digite um Resultado Válido, menor que 7 e maior que 0: ")
			leia(D)
			}
		
		escreva("Insira o número de linhas da Matriz B: ")
		leia(E)
		enquanto(E < 1 ou E > 6) {
			escreva("Digite um Resultado Válido, menor que 7 e maior que 0: ")
			leia(E)
			}
		escreva("Insira o número de colunas da Matriz B: ")
		leia(F)
		enquanto(F < 1 ou F > 6) {
			escreva("Digite um Resultado Válido, menor que 7 e maior que 0: ")
			leia(F)
			}

		// Caso a Matriz Não puder ser multiplicada.
		se(D != E){
			escreva("O número de Colunas de A é Diferente do número de Linhas de B \n")
			escreva("Portanto, essa multiplicação de matrizes Não é Possível! \n")
			}

		// Entrada de Valores por parte do usuário,
		// Preenche as informações das matrizes
		senao{
			para (l = 0; l < C ; l++){
				para (c = 0 ; c < D ; c++){
				escreva("Informe o elemento ",l,"x", c," da matriz A: ")
				leia(A[l][c])
			}
		}
		
		para (l = 0; l < E ; l++)
		{
			para (c = 0 ; c < F ; c++)
			{
				escreva("Informe o elemento ",l,"x",c," da Segunda matriz: ")
				leia(B[l][c])
			}
		}
			
		// Imprime na tela as Matrizes A e B, respectivamente	
		escreva("Matriz A: \n")
		para (l = 0; l < C ; l++)
		{
			para (c = 0 ; c < D ; c++)
			{
				escreva("[",A[l][c],"]")
			}
			escreva("\n")
		}
		
		escreva("Matriz B: \n")
		para (l = 0; l < C ; l++)
		{
			para (c = 0 ; c < D ; c++)
			{
				escreva("[",B[l][c],"]")
			}
			escreva("\n")
		}

		// Faz o cálculo da Matriz 'Multiplicação'
		para (l = 0; l < C ; l++){
			para (c = 0 ; c < F ; c++){
				multi_aux = 0.0
				para(contador = 0; contador < D; contador++){
					multi_aux = multi_aux + (A[l][contador] * B[contador][c])
					}
				MULTI[l][c] = multi_aux
			}
		}


		// Imprime na tela a Matriz Multiplicação
		escreva("Matriz 'MULTIPLICAÇÃO' = AxB (GCxF): \n")

		para (l = 0; l < C ; l++){
			para (c = 0 ; c < F ; c++){
				escreva("[",MULTI[l][c],"]")
				}
			escreva("\n")
			}
			
		}
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1764; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {A, 12, 7, 1}-{B, 12, 16, 1};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */