// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser
// lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e
// imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido 
// (UTILIZANDO ENQUANTO).

programa
{
	funcao inicio() 
	{	
		// Declaração de Variáveis
		real valor1, valor2

		// Entrada dos Valores por parte do usuário
		escreva("Digite o Valor 1: ")
		leia(valor1)

		escreva("Digite o Valor 2: ")
		leia(valor2)

		// Caso o usuário tente digitar 0 para o denominador, o programa repete o pedido de entrada
		enquanto(valor2 == 0){
			escreva("Entrada Inválida, Digite o Valor 2 Novamente: ")
			leia(valor2)
			}

		// Imprime na tela o resultado da divisão
		escreva("O resultado da divisão: ", valor1, " / ", valor2, " = ", valor1/valor2)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 835; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */