// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 5) Criar um algoritmo em PORTUGOL que informe a quantidade total de calorias de uma
// refeição a partir do usuário que deverá informar o prato, a sobremesa e a bebida 
// (veja a tabela a seguir).

// Prato Calorias Sobremesa Calorias Bebida Calorias
// Vegetariano 180 cal Abacaxi 75 cal Chá gelado 20 cal
// Peixe 230 cal Sorvete diet 110 cal Suco de laranja 70 cal
// Frango 250 cal Mouse diet 170 cal Suco de melão 100 cal
// Carne 350 cal Mouse chocolate 200 cal Refrigerante diet 65 cal

programa
{
	funcao inicio() 
	{
		// Declaração e inicialização de variáveis
		inteiro opcao, cal_prato = 0, cal_sobremesa = 0, cal_bebida = 0
		real calorias_totais 
		cadeia prato = "", sobremesa = "", bebida = ""
		
		// Entrada das opções por parte do usuário ( Prato )
		escreva(" - Pratos - \n")
		escreva("1 - Vegetariano\n")
		escreva("2 - Peixe\n")
		escreva("3 - Frango\n")
		escreva("4 - Carne\n")
		escreva("Escolha uma opção: ")
		leia(opcao)

		// Caso o Usuário Digite uma opção fora da lista, o programa repete a entrada de opções.
		enquanto(opcao < 1 ou opcao > 4){
			escreva("Opção Inválida! Digite Novamente: ")
			leia(opcao)
			}

		// Relacionando a Opção Escolhida ao Prato e Calorias.
		escolha (opcao)	
		{
			caso 1:
				prato = "Vegetariano"
		 		cal_prato = 180
		 		pare  
		 	caso 2: 
		 		prato = "Peixe"
		 		cal_prato = 230
		 		pare   
		 	caso 3: 
		 		prato = "Frango"
		 		cal_prato = 250
		 		pare
		 	caso 4:
		 		prato = "Carne"
		 		cal_prato = 350
		 		pare
		}
		
		limpa()
		escreva (prato, " Escolhido(a) como Prato! \n")

		// Entrada das opções por parte do usuário ( Sobremesa )
		escreva(" - Sobremesas - \n")
		escreva("1 - Abacaxi\n")
		escreva("2 - Sorvete Diet\n")
		escreva("3 - Mouse Diet\n")
		escreva("4 - Mouse Chocolate\n")
		escreva("Escolha uma opção: ")
		leia(opcao)

		// Caso o Usuário Digite uma opção fora da lista, o programa repete a entrada de opções.
		enquanto(opcao < 1 ou opcao > 4){
			escreva("Opção Inválida! Digite Novamente: ")
			leia(opcao)
			}

		// Relacionando a Opção Escolhida à Sobremesa e Calorias.
		escolha (opcao)	
		{
			caso 1:
				sobremesa = "Abacaxi"
		 		cal_sobremesa = 75
		 		pare  
		 	caso 2: 
		 		sobremesa = "Sorvete Diet"
		 		cal_sobremesa = 110
		 		pare   
		 	caso 3: 
		 		sobremesa = "Mouse Diet"
		 		cal_sobremesa = 170
		 		pare
		 	caso 4:
		 		sobremesa = "Mouse Chocolate"
		 		cal_sobremesa = 200
		 		pare
		}

		limpa()
		escreva (sobremesa, " Escolhido(a) como Sobremesa! \n")

		// Entrada das opções por parte do usuário ( Bebida )
		escreva(" - Bebidas - \n")
		escreva("1 - Chá Gelado\n")
		escreva("2 - Suco de Laranja\n")
		escreva("3 - Suco de Melão\n")
		escreva("4 - Refrigerante Diet\n")
		escreva("Escolha uma opção: ")
		leia(opcao)

		// Caso o Usuário Digite uma opção fora da lista, o programa repete a entrada de opções.
		enquanto(opcao < 1 ou opcao > 4){
			escreva("Opção Inválida! Digite Novamente: ")
			leia(opcao)
			}

		// Relacionando a Opção Escolhida à Bebida e Calorias.
		escolha (opcao)	
		{
			caso 1:
				bebida = "Chá Gelado"
		 		cal_bebida = 20
		 		pare  
		 	caso 2: 
		 		bebida = "Suco de Laranja"
		 		cal_bebida = 70
		 		pare   
		 	caso 3: 
		 		bebida = "Suco de Melão"
		 		cal_bebida = 100
		 		pare
		 	caso 4:
		 		bebida = "Refrigerante Diet"
		 		cal_bebida = 65
		 		pare
		}

		limpa()
		escreva (bebida, " Escolhido(a) como Bebida! \n\n")

		calorias_totais = cal_prato + cal_sobremesa + cal_bebida

		escreva("Refeição escolhida: \n")
		escreva(prato, ": ", cal_prato, " Cal \n")
		escreva(sobremesa, ": ", cal_sobremesa, " Cal \n")
		escreva(bebida, ": ", cal_bebida, " Cal \n\n")
		
		escreva("Totalizando: ", calorias_totais, " Calorias \n\n")

		escreva("Boa refeição! Volte sempre!")

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 788; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */