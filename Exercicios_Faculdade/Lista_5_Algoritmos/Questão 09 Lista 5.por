// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 9) Uma agência de uma cidade do interior tem, no máximo, 10000 clientes. 
// Criar um algoritmo em PORTUGOL que possa receber:
// O número da conta, nome e saldo de cada cliente.
 
// Esse algoritmo deve imprimir todas as contas, os respectivos saldos e uma das
// mensagens: positivo/negativo. 

// A digitação acaba quando se digita –999 para um número da conta 
// ou quando chegar a 10000. 

// Ao final, deverá sair o total de clientes com saldo negativo,
// o total de clientes da agência e o saldo da agência.


programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro conta_cliente[10000], contador, 
	contador_total_clientes = 0, total_clientes_negativados = 0, 
	aux

	real saldo_cliente[10000], saldo_agencia = 0

	cadeia nome_cliente[10000], situacao_conta_cliente[10000]
	
	// Entrada dos Valores por parte do usuário + Processamento de dados
	escreva("Inicializando Cadastro de Conta Bancária! \n\n")
	enquanto(contador_total_clientes < 10000){

		escreva("Digite o Número da Conta do Novo Cliente (ou -999 para encerrar): ")
		leia(conta_cliente[contador_total_clientes])

		se(conta_cliente[contador_total_clientes] == -999) {
			pare
			}

		escreva("Digite o Nome do ",contador_total_clientes+1,"º Cliente: ")
		leia(nome_cliente[contador_total_clientes])

		escreva("Digite o Saldo Atual da Conta: ")
		leia(saldo_cliente[contador_total_clientes])

		se(saldo_cliente[contador_total_clientes] >= 0){
			situacao_conta_cliente[contador_total_clientes] = "Positivo"
		}
		senao{
			situacao_conta_cliente[contador_total_clientes] = "Negativo"
			total_clientes_negativados = total_clientes_negativados + 1
			}

		saldo_agencia = saldo_agencia + saldo_cliente[contador_total_clientes]
		
		escreva("Conta Bancaria do(a): ", nome_cliente[contador_total_clientes], " Cadastrada com Sucesso! \n")
		escreva("Re-Inicializando o programa... \n")
		
		contador_total_clientes = contador_total_clientes + 1
			
		}

	//Imprime na tela as informações
	se(contador_total_clientes == 0 ){
		escreva("Nenhum cliente cadastrado no sistema!\n")
		}
	
	// Imprime todas as informações de todos os clientes, pode comentar essa parte
	// do código, caso deseje não mostrar essas informações ao final da execução
	para(contador = 0; contador < contador_total_clientes; contador++){
		escreva("\nNúmero da Conta: ", conta_cliente[contador], 
		"\nNome Do Cliente: ", nome_cliente[contador],
		"\nSaldo Atual Do Cliente: ", saldo_cliente[contador],
		"\nSituação da Conta: ", situacao_conta_cliente[contador], "\n\n")
		}

	// Imprime as informações chaves da agência
	escreva("Total de Clientes Negativados: ", total_clientes_negativados, "\n")
	escreva("Total de Clientes Cadastrados na Agência: ", contador_total_clientes, "\n")
	escreva("Saldo da Agência: ", saldo_agencia, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2134; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */