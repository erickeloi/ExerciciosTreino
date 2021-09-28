// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 11) Em uma eleição existem 4 candidatos.
// Os votos são informados por meio de código. 
// Os códigos utilizados são:

// 1,2,3,4 Votos para os respectivos Candidatos
// 5 Voto Nulo
// 6 Voto em Branco

// Faça um algoritmo em PORTUGOL para calcular e mostrar:

// O total de votos para cada candidato
// O total de votos nulos
// O total de votos brancos
// O percentual de votos nulos sobre o total de votos
// O percentual de votos branco sobre o total de votos
// Total de votantes que votaram

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro votos_candidato1 = 0, votos_candidato2 = 0, 
	votos_candidato3 = 0, votos_candidato4 = 0,
	voto_aux = 0, option_aux, votos_totais

	real votos_nulos = 0.0, votos_brancos = 0.0, 
	percent_nulo = 0.0, percent_branco = 0.0

	logico option = verdadeiro

	
	// Entrada dos Valores por parte do usuário 
	escreva("Inicializando Sistema de Votação... \n")
	
	enquanto(option){
		escreva("Digite 1 para Votar no Canditado 1 \n")
		escreva("Digite 2 para Votar no Canditado 2 \n")
		escreva("Digite 3 para Votar no Canditado 3 \n")
		escreva("Digite 4 para Votar no Canditado 4 \n")
		escreva("Digite 5 para Votar Nulo \n")
		escreva("Digite 6 para Votar Branco \n")
		escreva("Sua Opção: ")
		leia(voto_aux)

		enquanto(voto_aux < 1 ou voto_aux > 6){
			escreva("Opção Inválida, Digite sua Opção novamente:")
			leia(voto_aux)
		}

		se(voto_aux == 1){
			votos_candidato1 = votos_candidato1 + 1
			escreva("Candidato 1 Escolhido !!!")
		}
		senao se(voto_aux == 2){
			votos_candidato2 = votos_candidato2 + 1
			escreva("Candidato 2 Escolhido !!!")
			}
		senao se(voto_aux == 3){
			votos_candidato3 = votos_candidato3 + 1
			escreva("Candidato 3 Escolhido !!!")
			}
		senao se(voto_aux == 4){
			votos_candidato4 = votos_candidato4 + 1
			escreva("Candidato 4 Escolhido !!!")
			}
		senao se(voto_aux == 5){
			votos_nulos = votos_nulos + 1
			escreva("Voto Nulo !!!")
			}
		senao se(voto_aux == 6){
			votos_brancos = votos_brancos + 1
			escreva("Voto Branco !!!")
			}

		escreva("\nVoto Computado Com Sucesso !!!\n")

		// Menu - Caso o usuário queira votar denovo, 
		// ou fechar o programa e cálcular os resultados.
		escreva("Se Deseja Votar Novamente, Digite 1\n")
		escreva("Se Deseja Fechar o sistema de votação e mostrar os resultados, Digite 0\n")
		escreva("1 - Votar Denovo\n0 - Termina a votação\nSua Opção: ")
		leia(option_aux)
		enquanto(option_aux < 0 ou option_aux > 1){
			escreva("Opção Inválida, Digite novamente: ")
			leia(option_aux)
			}
		se(option_aux == 0){
			option = falso
			}
		}
	// Processamento de Dados
	escreva("Processando Dados... \n")

	votos_totais = (votos_candidato1 + votos_candidato2 + votos_candidato3 + votos_candidato4 + votos_nulos + votos_brancos)

	percent_nulo = (votos_nulos/votos_totais) * 100

	percent_branco = (votos_brancos/votos_totais) * 100

	//Imprime na tela os resultados

	escreva("Resultados do Sistema de Votação! \n")
	escreva("Total de Votos pro Candidato 1: ", votos_candidato1, " \n")
	escreva("Total de Votos pro Candidato 2: ", votos_candidato2, " \n")
	escreva("Total de Votos pro Candidato 3: ", votos_candidato3, " \n")
	escreva("Total de Votos pro Candidato 4: ", votos_candidato4, " \n")
	escreva("Total de Votos Nulos: ", votos_nulos, " \n")
	escreva("Total de Votos Brancos: ", votos_brancos, " \n")

	escreva("Porcentagem de Votos Nulos: ", percent_nulo, " % \n")
	escreva("Porcentagem de Votos Brancos: ", percent_branco, " % \n")

	escreva("Total de Votos: ", votos_totais)
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2684; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */