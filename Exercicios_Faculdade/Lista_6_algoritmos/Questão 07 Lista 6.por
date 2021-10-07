// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex.07
// Cadastrar 50 tipos de plantas

// Cada planta no "Banco de Dados" deve possuir:
// - Nome
// - Estoque Ideal
// - Estoque Atual

programa {
	funcao inicio() {
		
		// Declaração de variáveis
		
		// Vizando facilitar o teste desse algoritmo,
		// O programador pode mudar o 'valor padrão'
		// da Quantidade de Plantas, atualmente, o valor padrão é 50

		// Exemplo: qnt_plantas = 3
		const inteiro qnt_plantas = 50
		
		cadeia plantas[qnt_plantas]
		
		inteiro estoque[qnt_plantas][2],
		estoques_baixo[qnt_plantas], contador_estoque_baixo = 0,
		c, indice, qnt
		
		// Entrada dos Valores por parte do usuário
		para(c = 0; c < qnt_plantas; c++){
			escreva("Digite o Nome da Planta Nº", c,": ")
			leia(plantas[c])

			escreva("Digite o Estoque Ideal da '", plantas[c],"'(Unid.): ")
			leia(estoque[c][0])
			
			escreva("Digite o Estoque Atual da '", plantas[c],"'(Unid.): ")
			leia(estoque[c][1])

			// Ele guarda a Linha/Indice da Matriz que está com o estoque
			// Abaixo do Ideal.
			se(estoque[c][1] < estoque[c][0]){
				estoques_baixo[contador_estoque_baixo] = c
				contador_estoque_baixo++
				}
			}
			
		escreva("\n\n")
		// Imprime na tela
		se(contador_estoque_baixo > 0){
			para(c=0;c < contador_estoque_baixo; c++){
				indice = estoques_baixo[c]
				qnt = estoque[indice][0] - estoque[indice][1]

				escreva("Atenção!!! \n")
				escreva("A planta de Nome: ",plantas[indice]," \n")
				
				escreva("Está com o Estoque Abaixo do Ideal! \n")
				escreva("Estoque Ideal: ", estoque[indice][0]," \n")
				escreva("Estoque Atual: ", estoque[indice][1]," \n")
				
				escreva("Portanto, Você precisa comprar amanhã mais ",qnt," Plantas desse tipo, \n")
				escreva("para bater o estoque ideal. \n\n")
				}
			}
		senao{
			escreva("Estoque em dia, não é necessário comprar mais plantas amanhã! \n")
			}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 499; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {plantas, 24, 9, 7};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */