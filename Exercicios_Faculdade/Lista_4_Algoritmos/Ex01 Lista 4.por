// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 1) Dados três valores A, B e C, construa um algoritmo em PORTUGOL, 
// que imprima os valores de forma Ascendente (do menor para o maior).

programa
{
	
	funcao inicio()
	{	
		// Declaração de Variáveis
		real A, B, C
		
		// Entrada dos Valores por parte do usuário
		escreva("Insira o valor de A: ")
		leia(A)

		escreva("Insira o valor de B: ")
		leia(B)

		escreva("Insira o valor de C: ")
		leia(C)

		escreva("A Ordem Crescente desses números é: \n")
		// Verificação e Impressão na tela ( Todos os 6 casos )
		// ( A > B > C )
		se ((A > B) e (B > C) e (A > C)){
			escreva("3° ", A,"\n2° ", B,"\n1° ", C)
			}
		// ( A > C > B)
		senao se((A > C) e ( C > B) e (A > B)){
			escreva("3° ", A,"\n2° ", C,"\n1° ", B)
			}
		// (B > A > C)
		senao se ((B > A) e (B > C) e (A > C)){
			escreva("3° ", B,"\n2° ", A,"\n1° ", C)
			}
		// (B > C > A)
		senao se((B>C) e (B>A) e (C>A)){
			escreva("3° ", B,"\n2° ", C,"\n1° ", A)
			}
		// (C > A > B)
		senao se((C>A) e (C>B) e (A>B)){
			escreva("3° ", C,"\n2° ", A,"\n1° ", B)
			}
		// (C > B > A)
		senao se((C>B) e (C>A) e (B>A)){
			escreva("3° ", C,"\n2° ", B,"\n1° ", A)
			}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 179; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */