// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 8) Uma startup de 4 anos de alunos da FACOMP/UFPA depois de uma rodada de investimento,
// resolveu dar aumento de salários aos seus colaboradores, então resolveram criar um
// programa que calcule os reajustes de acordo com tempo de contribuição na startup.

// Colaboradores Qtd.
// Estagiário   6
// Analista     10
// Gerente      3
// CEO/COO      2

// a. Existe 3 faixas salariais antes do aumento: Estagiário – R$1200,00; Analista –
// R$3500,00; Gerente – R$5500,00 e CEO e COO – R$6700,00

// b. Para quem mais de 3 anos, vai receber 15% de aumento

// c. Para quem está há 2 anos ou mais* e até 3 anos, vai receber 10% de aumento
// ( o texto estava meio estranho, então eu fiz essa correção * ) 

// d. Para quem tem menos de 2 anos vai receber 5% de aumento

// O programa vai receber a função do colaborador e o tempo e imprimir na tela quanto vai o
// total que vai receber.

//PS: Guardar o valor total de salários pagos sem e com aumento – BÔNUS – 1pts

programa
{
	
	funcao inicio()
	{
		// Declarando Vetores e Variáveis ( Basicamente um Banco de dados a essa altura do campeonato )
		const inteiro qntd_estagiarios = 6, qntd_analistas = 10, qntd_gerentes = 3, qntd_ceocoo = 2,
		salario_estagiario = 1200, salario_analista = 3500, salario_gerente = 5500, salario_ceocoo = 6700

		inteiro total_pago, contador,
		opcao_principal = 0, opcao_secundaria = 0, tipo_colaborador = 0,
		contador_estagiario = 0, contador_analista = 0, contador_gerente = 0, contador_ceocoo = 0

		real anos_de_contribuicao, aux, total_pago_aumento = 0, total_auxiliar = 0,
		anos_empregado_estagiarios[6], anos_empregado_analistas[10], anos_empregado_gerente[3], anos_empregado_ceocoo[2],
		salario_novo_estagiario[6], salario_novo_analista[10], salario_novo_gerente[3], salario_novo_ceocoo[2]

		// Menu caso o usuário deseja adicionar um colaborador e seu tempo de empresa.
		enquanto(opcao_principal != 2){
			escreva("\nDeseja Adicionar os Anos De Empresa de um determinado Colaborador? \n")
			escreva("Digite '1' para 'Sim' ou Digite '2' para 'Não': ")
			leia(opcao_principal)
			
			enquanto(opcao_principal < 1 ou opcao_principal > 2) {
				escreva("Digite '1' para 'Sim' ou Digite '2' para 'Não': ")
				leia(opcao_principal)
				}

			// Opção 1 - SIM
			
			// Coleta de informação do(s) colaborador(es) por parte do usuário
			se (opcao_principal == 1) {
			escreva("1 - ESTAGIÁRIO \n")
			escreva("2 - Analista \n")
			escreva("3 - Gerente \n")
			escreva("4 - CEO/COO \n")
			
			escreva("Selecione a função desse colaborador: ")
			leia(tipo_colaborador)

			// Caso o usuário digite um colaborador inexistente, o programa repete a entrada
			enquanto(tipo_colaborador < 1 ou tipo_colaborador > 4) {
				escreva("Entrada Inválida, Selecione a função desse colaborador: ")
				leia(tipo_colaborador)
				}

			// ESTAGIÁRIO SELECIONADO
			se (tipo_colaborador == 1) {
				
				se (contador_estagiario > 5) {
					// Limite de Funcionarios ( 6 estagiarios )
					escreva("Limite de Estagiarios já alcançado, voltando ao menu inicial")
					}
				senao {
					// Usuário adiciona os anos de contribuição do colaborador
					
					// E a Quantidade de Colaboradores é computada para não ser adicionados 
					// Colaboradores A Mais do que a empresa emprega
					
					escreva("ESTAGIÁRIO NÚMERO :", contador_estagiario, " \n")
					escreva("Digite o(s) ano(s) de contribuição desse estagiário :")
					leia(anos_de_contribuicao)

					anos_empregado_estagiarios[contador_estagiario] = anos_de_contribuicao

					escreva("Anos de contribuicao adicionados com sucesso!!!")

					contador_estagiario++
					}
			}

			// ANALISTA SELECIONADO
			senao se (tipo_colaborador == 2) {
				
				se (contador_analista > 9) {
					// Limite de Funcionarios ( 10 Analistas )
					escreva("Limite de Analistas já alcançado, voltando ao menu inicial")
					}
				senao {
					// Usuário adiciona os anos de contribuição do colaborador
					
					// E a Quantidade de Colaboradores é computada para não ser adicionados 
					// Colaboradores A Mais do que a empresa emprega
					escreva("ANALISTA NÚMERO :", contador_analista, " \n")
					escreva("Digite o(s) ano(s) de contribuição desse Analista :")
					leia(anos_de_contribuicao)

					anos_empregado_analistas[contador_analista] = anos_de_contribuicao

					escreva("Anos de contribuicao adicionados com sucesso!!!")

					contador_analista++
					}
			}
			senao se (tipo_colaborador == 3) {
				
				se (contador_gerente > 2) {
					// Limite de Funcionarios ( 3 Gerentes )
					escreva("Limite de Gerentes já alcançado, voltando ao menu inicial")
					}
				senao {
					// Usuário adiciona os anos de contribuição do colaborador
					
					// E a Quantidade de Colaboradores é computada para não ser adicionados 
					// Colaboradores A Mais do que a empresa emprega
					escreva("GERENTE NÚMERO :", contador_gerente, " \n")
					escreva("Digite o(s) ano(s) de contribuição desse Gerente :")
					leia(anos_de_contribuicao)

					anos_empregado_gerente[contador_gerente] = anos_de_contribuicao

					escreva("Anos de contribuicao adicionados com sucesso!!!")

					contador_gerente++
					}
					
				}
			senao se (tipo_colaborador == 4) {
				
				se (contador_ceocoo > 1) {
					// Limite de Funcionarios ( 2 CEO / COO )
					escreva("Limite de CEO/COO já alcançado, voltando ao menu inicial")
					}
				senao {
					// Usuário adiciona os anos de contribuição do colaborador
					
					// E a Quantidade de Colaboradores é computada para não ser adicionados 
					// Colaboradores A Mais do que a empresa emprega
					escreva("CEO/COO NÚMERO :", contador_ceocoo, " \n")
					escreva("Digite o(s) ano(s) de contribuição desse CEO/COO :")
					leia(anos_de_contribuicao)

					anos_empregado_ceocoo[contador_ceocoo] = anos_de_contribuicao

					escreva("Anos de contribuicao adicionados com sucesso!!!")

					contador_ceocoo++
					}
					
				}
			
			
			} 
		}
		// Imprime na tela os resultados ( Sem aumento )
		
		escreva("Total de Salários pagos à cada colaborador, Sem aumento: \n")
		escreva("Estagiário: ", qntd_estagiarios * salario_estagiario, " \n")
		escreva("Analista: ", qntd_analistas * salario_analista, " \n")
		escreva("Gerente: ", qntd_gerentes * salario_gerente, " \n")
		escreva("CEO/COO: ", qntd_ceocoo * salario_ceocoo, " \n")

		total_pago = qntd_ceocoo * salario_ceocoo + qntd_gerentes * salario_gerente + qntd_analistas * salario_analista + qntd_estagiarios * salario_estagiario 
		
		
		escreva("Total pago aos Colaboradores, antes do aumento: ", total_pago, " \n")

		// Caso o usuário tenha adicionado um colaborador com tempo de empresa!
		se(contador_estagiario > 0 ou contador_analista > 0 ou contador_gerente > 0 ou contador_ceocoo > 0) {
			se (contador_estagiario > 0) {
				
				// Caso for adicionado o tempo de empresa desse tipo de colaborador...
				
				escreva("Imprimindo Resultados Sobre A Atualização de Salarios dos Estagiários... \n")
				para(contador = 0; contador < contador_estagiario; contador++){
					// O programa percorre a lista de "anos empregado" desse colaborador e calcula a porcentagem de aumento no salário
					se (anos_empregado_estagiarios[contador] < 2) {
						// 2 anos ou menos de empresa, aumento de 5%
						salario_novo_estagiario[contador] = salario_estagiario + (salario_estagiario * 0.05)
						}
					senao se(anos_empregado_estagiarios[contador] >= 2 e anos_empregado_estagiarios[contador] <= 3){
						// 2 <= Tempo de empresa <= 3, Aumento de 10%
						salario_novo_estagiario[contador] = salario_estagiario + (salario_estagiario * 0.1)
						}
					senao {
						// Mais de 3 anos de empresa, aumento de 15%
						salario_novo_estagiario[contador] = salario_estagiario + (salario_estagiario *  0.15)
						}

					// Imprime na tela o Número do Funcionario e seu novo salário ( Com acrescimo )
					escreva("Estagiário Número '",contador, "'", " : ", salario_novo_estagiario[contador], " \n" )
					}

					// Guarda o novo salario total em uma variavel para ajudar nos calculos
					aux = 0
					para(contador = 0; contador < contador_estagiario; contador++){
						aux = aux + salario_novo_estagiario[contador]
						}
					
					// Total auxiliar = Total pago pela empresa aos colaboradores desse tipo específico
					
					// Total pago aumento = Guarda o Total pago pela empresa a todos os colaboradores
					total_auxiliar = (((qntd_estagiarios * salario_estagiario) - contador_estagiario * salario_estagiario) + aux)
					total_pago_aumento = total_pago_aumento + total_auxiliar
					escreva("Total pago, com aumento, aos Estagiários: ", total_auxiliar, " \n")

					
				 
				}
			se (contador_analista > 0) {

				// Caso for adicionado o tempo de empresa desse tipo de colaborador...
				
				escreva("Imprimindo Resultados Sobre A Atualização de Salarios dos Analistas... \n")
				para(contador = 0; contador < contador_analista; contador++){
					
					se (anos_empregado_analistas[contador] < 2) {
						// 2 anos ou menos de empresa, aumento de 5%
						salario_novo_analista[contador] = salario_analista + (salario_analista * 0.05)
						}
					senao se(anos_empregado_analistas[contador] >= 2 e anos_empregado_analistas[contador] <= 3){
						// 2 <= Tempo de empresa <= 3, Aumento de 10%
						salario_novo_analista[contador] = salario_analista + (salario_analista * 0.1)
						}
					senao {
						// Mais de 3 anos de empresa, aumento de 15%
						salario_novo_analista[contador] = salario_analista + (salario_analista *  0.15)
						}
					// Imprime na tela o Número do Funcionario e seu novo salário ( Com acrescimo )
					escreva("Analista Número '",contador, "'", " : ", salario_novo_analista[contador], " \n" )
					}

					// Guarda o novo salario total em uma variavel para ajudar nos calculos
					aux = 0
					para(contador = 0; contador < contador_analista; contador++){
						aux = aux + salario_novo_analista[contador]
						}
					// Total auxiliar = Total pago pela empresa aos colaboradores desse tipo específico
					
					// Total pago aumento = Guarda o Total pago pela empresa a todos os colaboradores
					total_auxiliar = (((qntd_analistas * salario_analista) - contador_analista * salario_analista) + aux)
					total_pago_aumento = total_pago_aumento + total_auxiliar
					escreva("Total pago, com aumento, aos Analistas: ", total_auxiliar, " \n")

					
				 
				}
			se (contador_gerente > 0) {

				// Caso for adicionado o tempo de empresa desse tipo de colaborador...
				
				escreva("Imprimindo Resultados Sobre A Atualização de Salarios dos Gerentes... \n")
				para(contador = 0; contador < contador_gerente; contador++){
					
					se (anos_empregado_gerente[contador] < 2) {
						// 2 anos ou menos de empresa, aumento de 5%
						salario_novo_gerente[contador] = salario_gerente + (salario_gerente * 0.05)
						}
					senao se(anos_empregado_gerente[contador] >= 2 e anos_empregado_gerente[contador] <= 3){
						// 2 <= Tempo de empresa <= 3, Aumento de 10%
						salario_novo_gerente[contador] = salario_gerente + (salario_gerente * 0.1)
						}
					senao {
						// Mais de 3 anos de empresa, aumento de 15%
						salario_novo_gerente[contador] = salario_gerente + (salario_gerente *  0.15)
						}
					// Imprime na tela o Número do Funcionario e seu novo salário ( Com acrescimo )
					escreva("Gerente Número '",contador, "'", " : ", salario_novo_gerente[contador], " \n" )
					}
					// Guarda o novo salario total em uma variavel para ajudar nos calculos
					aux = 0
					para(contador = 0; contador < contador_gerente; contador++){
						aux = aux + salario_novo_gerente[contador]
						}
					// Total auxiliar = Total pago pela empresa aos colaboradores desse tipo específico
					
					// Total pago aumento = Guarda o Total pago pela empresa a todos os colaboradores
					total_auxiliar =  (((qntd_gerentes * salario_gerente) - contador_gerente * salario_gerente) + aux)
					total_pago_aumento = total_pago_aumento + total_auxiliar
					escreva("Total pago, com aumento, aos Gerentes: ", total_auxiliar, " \n")

				
				 
				}
			se (contador_ceocoo > 0) {

				// Caso for adicionado o tempo de empresa desse tipo de colaborador...
				
				escreva("Imprimindo Resultados Sobre A Atualização de Salarios dos CEO/COO... \n")
				para(contador = 0; contador < contador_ceocoo; contador++){
					
					se (anos_empregado_ceocoo[contador] < 2) {
						// 2 anos ou menos de empresa, aumento de 5%
						salario_novo_ceocoo[contador] = salario_ceocoo + (salario_ceocoo * 0.05)
						}
					senao se(anos_empregado_ceocoo[contador] >= 2 e anos_empregado_ceocoo[contador] <= 3){
						// 2 <= Tempo de empresa <= 3, Aumento de 10%
						salario_novo_ceocoo[contador] = salario_ceocoo + (salario_ceocoo * 0.1)
						}
					senao {
						// Mais de 3 anos de empresa, aumento de 15%
						salario_novo_ceocoo[contador] = salario_ceocoo + (salario_ceocoo *  0.15)
						}
					// Imprime na tela o Número do Funcionario e seu novo salário ( Com acrescimo )
					escreva("CEO/COO Número '",contador, "'", " : ", salario_novo_ceocoo[contador], " \n" )
					}
					// Guarda o novo salario total em uma variavel para ajudar nos calculos
					aux = 0
					para(contador = 0; contador < contador_ceocoo; contador++){
						aux = aux + salario_novo_ceocoo[contador]
						}
					// Total auxiliar = Total pago pela empresa aos colaboradores desse tipo específico
					
					// Total pago aumento = Guarda o Total pago pela empresa a todos os colaboradores
					total_auxiliar = (((qntd_ceocoo * salario_ceocoo) - contador_ceocoo * salario_ceocoo) + aux)
					total_pago_aumento = total_pago_aumento + total_auxiliar
					escreva("Total pago, com aumento, aos CEO/COO: ", total_auxiliar, " \n")

					escreva("\n DEBUG: Total_pago_aumento: ", total_pago_aumento)
				 
				}

				// Para o total_pago_aumento continuar mostrando o valor correto caso o usuário não inserir determinado colaborador
				se (contador_estagiario == 0 ){
					total_pago_aumento = total_pago_aumento + 7200
					}
				se (contador_analista == 0 ){
					total_pago_aumento = total_pago_aumento + 35000
					}
				se (contador_gerente == 0 ){
					total_pago_aumento = total_pago_aumento + 16500
					}
				se (contador_ceocoo == 0 ){
					total_pago_aumento = total_pago_aumento + 13400
					}
			// Imprime na tela o total pago pela empresa aos colaboradores ( Após o aumento )
			escreva("\n \nEm Resumo, o total pago pela empresa aos colaboradores, após o aumento, foi de: ", total_pago_aumento, "R$ \n \n")
			
			}

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1642; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */