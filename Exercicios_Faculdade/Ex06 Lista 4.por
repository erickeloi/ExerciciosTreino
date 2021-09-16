// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 6) Criar um algoritmo em PORTUGOL que leia o um número inteiro entre 1 e 7 e escreva o dia
// da semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá
// aparecer uma mensagem informando que não existe dia da semana com esse número
programa
{
	
	funcao inicio()
	{
		// Declaração de variáveis
		inteiro numero
		cadeia dia = ""

		// Entrada dos Valores por parte do usuário
		escreva("Digite um número de 1 a 7 para saber o dia da semana correspondente a esse número: ")
		leia(numero)

		// Caso o usuário digitar um número inválido, o programa repete a entrada
		enquanto(numero < 1 ou numero > 7){
			escreva("Número inválido ! Digite um número de 1 a 7: ")
			leia(numero)
			}

		// Associa o número Digitado ao dia da semana
		se(numero == 1){
			dia = "Domingo"
			}
		senao se(numero == 2){
			dia = "Segunda"
			}
		senao se(numero == 3){
			dia = "Terça"
			}
		senao se(numero == 4){
			dia = "Quarta"
			}
		senao se(numero == 5){
			dia = "Quinta"
			}
		senao se(numero == 6){
			dia = "Sexta"
			}
		senao se(numero == 7){
			dia = "Sábado"
			}
			
		//Imprime na tela o  número digitado e o dia associado ao número.
		escreva("O dia da semana associado ao número '", numero, "'", " é: ", dia)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 276; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */