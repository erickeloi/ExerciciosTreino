// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 4) Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
// efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
// sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.


programa
{
	
	funcao inicio()
	{
		// Declaração de variáveis
		cadeia vendedor_nome
		real salario_fixo, salario_final, vendas_totais

		// Entrada dos Valores por parte do usuário
		escreva("Digite o nome do vendedor: ")
		leia(vendedor_nome)

		escreva("Digite o salário fixo desse vendedor: ")
		leia(salario_fixo)

		escreva("Digite o total de vendas (Em dinheiro): ")
		leia(vendas_totais)

		// Cálculo do Salário Final
		salario_final = salario_fixo + (vendas_totais * 0.15)

		//Imprime na tela Nome, Salário Fixo e Salário Final do mês
		
		escreva("Exibindo Informações do vendedor...\n")
		escreva("Nome do vendedor: ", vendedor_nome, "\n")
		escreva("Salário Fixo: ", salario_fixo, " R$", "\n")
		escreva("Salário Final (Acrescimo da comissão de vendas): ", salario_final, " R$")
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 604; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */