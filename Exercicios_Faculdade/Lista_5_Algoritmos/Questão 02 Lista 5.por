// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 2) A série de Fibonacci é formada pela sequência:
// 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
// Escreva um algoritmo em PORTUGAL,
// que gere a série de FIBONACCI até o (N) Enésimo termo (passado pelo usuário).

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro fibonacci, contador = 3, termo1 = 1, termo2 = 1, termo_aux
	
	// Entrada dos Valores por parte do usuário
	escreva("Digite o Termo que deseja ver da Sequencia de Fibonacci: ")
	leia(fibonacci)

	enquanto(fibonacci < 1){
		escreva("Digite um termo válido! Somente valores positivos: ")
		leia(fibonacci)
		}
	// Imprime na tela a série de fibonacci até o Termo que o usuário inserir
	se(fibonacci == 1){
		escreva("1, ")
		}
	senao se(fibonacci == 2){
		escreva("1, 1, ")
		}
	senao{
		escreva("1, 1, ")
		enquanto(contador <= fibonacci){
			termo_aux = termo1 + termo2
			escreva(termo_aux, ", ")
			termo1 = termo2
			termo2 = termo_aux
			contador += 1
		}
	}
	
		
	
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 771; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */