// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 5) Um cinema possui capacidade de 100 lugares e está sempre com ocupação total. 

// Certo dia, cada espectador respondeu a um questionário, no qual constava:
// - Sua idade
// - Sua opinião em relação ao filme, segundo as seguintes notas:

// NOTA | Significado
// A    |   Ótimo
// B    |   Bom
// C    |   Regular
// D    |   Ruim
// E    |   Péssimo

// Elabore um algoritmo que, lendo estes dados, calcule e imprima:

// - A quantidade de respostas Ótimas;
// - A diferença percentual entre respostas bom e regular;
// - A média de idade das pessoas que responderam ruim;
// - A diferença de idade das pessoas entre a maior idade que respondeu Ótimo e a
// maior idade que respondeu ruim

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	const inteiro qntd_espectadores = 100

	inteiro idade, option, 
	qntd_resp_otimo = 0,
	qntd_resp_ruim = 0, qntd_resp_pessimo = 0, dif_idade_resp_otimo_ruim = 0,
	contador_espectadores = 0, maior_idade_resp_otimo = 0, maior_idade_resp_ruim = 0

	real dif_percent_bom_regular = 0.0, media_idade_resp_ruim = 0.0,
	qntd_idade_resp_ruim = 0.0, qntd_resp_bom = 0.0, qntd_resp_regular = 0.0
	
	cadeia opiniao
	
	// Entrada dos Valores por parte do usuário
	enquanto(contador_espectadores < 100){
		escreva("Questionário do Cinema!!! \n\n")

		escreva("Digite sua idade: ")
		leia(idade)

		enquanto(idade < 0){
			escreva("Digite uma idade válida: ")
			leia(idade)
			}

		escreva("Qual foi sua opinião sobre o filme ? \n")
		escreva(" NOTA | Significado \n")
		escreva(" A    |   Ótimo \n")
		escreva(" B    |   Bom \n")
		escreva(" C    |   Regular \n")
		escreva(" D    |   Ruim \n")
		escreva(" E    |   Péssimo \n")

		escreva("Sua Resposta (Em Letra Maiúscula): ")
		leia(opiniao)

		enquanto(opiniao != "A" e opiniao != "B" e opiniao != "C" e opiniao != "D" e opiniao != "E"){
			escreva("Sua Resposta (Em Letra Maiúscula): ")
			leia(opiniao)
			}
			
		se(opiniao == "A"){
			qntd_resp_otimo++
			
			se(idade > maior_idade_resp_otimo){
				maior_idade_resp_otimo = idade
				}
			}
		senao se(opiniao == "B"){
			qntd_resp_bom++
			}
		senao se(opiniao == "C"){
			qntd_resp_regular++
			}
		senao se(opiniao == "D"){
			qntd_resp_ruim++
			qntd_idade_resp_ruim = qntd_idade_resp_ruim + idade
			
			se(idade > maior_idade_resp_ruim){
				maior_idade_resp_ruim = idade
				}
			}
		senao se(opiniao == "E"){
			qntd_resp_pessimo++
			}
		
		contador_espectadores++
		
		// Menu - Caso o usuário queira adicionar mais uma crﾃｭtica
		// Ou Sair do sistema e mostrar os resultados.
		escreva("\nQuestionário Respondido, Obrigado!!! Deseja Adicionar mais uma opinião?")
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
		
	// Processamento de Dados
	se(qntd_resp_bom > 0 ou qntd_resp_regular > 0){
		se((qntd_resp_bom > 0 e qntd_resp_regular == 0) ou (qntd_resp_regular > 0 e qntd_resp_bom == 0)){
			dif_percent_bom_regular = 100.0
			}
		senao{
		dif_percent_bom_regular = ((qntd_resp_bom/contador_espectadores) - (qntd_resp_regular/contador_espectadores)) * 100
			}
		}

	se(qntd_resp_ruim > 0){
	media_idade_resp_ruim = qntd_idade_resp_ruim/qntd_resp_ruim
	}
	
	se(maior_idade_resp_otimo > maior_idade_resp_ruim){
		dif_idade_resp_otimo_ruim = maior_idade_resp_otimo - maior_idade_resp_ruim
		}
	senao{
		dif_idade_resp_otimo_ruim = maior_idade_resp_ruim - maior_idade_resp_otimo
		}
		
	//Imprime na tela os Resultados
	escreva("Total de Respostas: ", contador_espectadores, " \n")
	escreva("Respostas Ótimas: ", qntd_resp_otimo, " \n")
	escreva("Diferença Percentual Entre as Respostas 'Bom' e 'Regular': ", dif_percent_bom_regular,"% \n")
	escreva("Média de idade das pessoas que responderam 'Ruim': ", media_idade_resp_ruim, " Anos \n\n")
	escreva("Diferença de idade entre os espectadores mais velhos que responderam com 'otimo' e 'ruim', respectivamente: \n")
	escreva("Eles possuem: ", dif_idade_resp_otimo_ruim, " Anos de Diferença de idade! \n")
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 3403; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */