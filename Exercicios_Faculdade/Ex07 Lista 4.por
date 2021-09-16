// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 7) Criar um algoritmo em PORTUGOL que leia um número inteiro entre 1 e 12 e escrever o
// mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá
// aparecer uma mensagem informando que não existe mês com este número.

programa
{
	
	funcao inicio()
	{
		// Declaração de variáveis
		inteiro numero
		cadeia mes = ""

		// Entrada dos Valores por parte do usuário
		escreva("Digite um número de 1 a 12 para saber o mês correspondente a esse número: ")
		leia(numero)

		// Caso o usuário digitar um número inválido, o programa repete a entrada
		enquanto(numero < 1 ou numero > 12){
			escreva("Número inválido ! Digite um número de 1 a 12: ")
			leia(numero)
			}

		// Associa o número Digitado ao mes da semana
		se(numero == 1){
			mes = "Janeiro"
			}
		senao se(numero == 2){
			mes = "Fevereiro"
			}
		senao se(numero == 3){
			mes = "Março"
			}
		senao se(numero == 4){
			mes = "Abril"
			}
		senao se(numero == 5){
			mes = "Maio"
			}
		senao se(numero == 6){
			mes = "Junho"
			}
		senao se(numero == 7){
			mes = "Julho"
			}
		senao se(numero == 8){
			mes = "Agosto"
			}
		senao se(numero == 9){
			mes = "Setembro"
			}
		senao se(numero == 10){
			mes = "Outubro"
			}
		senao se(numero == 11){
			mes = "Novembro"
			}
		senao se(numero == 12){
			mes = "Dezembro"
			}
			
		//Imprime na tela o  número digitado e o mes associado ao número.
		escreva("O mes associado ao número '", numero, "'", " é: ", mes)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 497; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */