// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 10) Criar um algoritmo em PORTUGOL que:
// Possa ler um conjunto de pedidos de compra e calcular o valor total da compra. 

// Cada pedido é composto pelos seguintes campos:
//  Número de pedido;
//  Data do pedido (dia, mês, ano);
//  Preço unitário;
//  Quantidade.

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro num_pedido, quantidade_pedido, option

	real preco_total = 0.0, preco_unit

	cadeia data_pedido
	
	// Entrada dos Valores por parte do usuário + Processamento de Dados
	enquanto(verdadeiro){
		option = 0

		// Entrada dos Valores por parte do usuário
		escreva("\nDigite o Número do Pedido: ")
		leia(num_pedido)
	
		escreva("Digite a Data do Pedido (DD/MM/AAAA): ")
		leia(data_pedido)
		
		escreva("Digite o Preço Unitário desse Produto, em Reais (R$): ")
		leia(preco_unit)

		enquanto(preco_unit < 0){
			escreva("Inválido! Somente valores Positivos\n")
			escreva("Digite o Preço Unitário desse Produto: ")
			leia(quantidade_pedido)
			}

		escreva("Digite a Quantidade Desejada desse produto: ")
		leia(quantidade_pedido)

		enquanto(quantidade_pedido < 0){
			escreva("Inválido! Somente valores Positivos\n")
			escreva("Digite a Quantidade Desejada desse produto: ")
			leia(quantidade_pedido)
			}
		// Processamento de Dados
		preco_total = preco_total + (preco_unit * quantidade_pedido)
		
		// Menu - Caso o usuário queira continuar a adicionar mais itens
		// Ou Sair do sistema e mostrar o resultado.
		escreva("\nPedido Anotado! Deseja Adicionar mais um produto?")
		escreva("\n1 - SIM,\n2 - NÃO\nSua Opção: ")
		leia(option)

		enquanto(option < 1 ou option > 2){
			escreva("\nDeseja Adicionar mais um produto?")
			escreva("\n1 - SIM,\n2 - NÃO\nSua Opção: ")
			leia(option)
			}

		se(option == 2){
			pare	
		}
	}

	//Imprime na tela o resultado
	escreva("\nCalculando... \n")
	escreva("\nO Preço de todos esses pedidos juntos é de: ", preco_total, "R$ \n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1880; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */