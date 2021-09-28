// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 7) Criar um algoritmo em PORTUGOL que: 
// calcule o M.M.C (mínimo múltiplo comum) entre dois números lidos. 

// (por exemplo: o M.M.C, entre 10 e 15 é 30).

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro num1, num2, mmc = 1, aux = 2, num_1_antigo, num_2_antigo
	
	
	escreva("Programa Cálculador de M.M.C ! \n\n")
	// Entrada dos Valores por parte do usuário
	escreva("Digite o Primeiro Número: ")
	leia(num1)
	escreva("Digite o Segundo Número: ")
	leia(num2)

	num_1_antigo = num1 
	num_2_antigo = num2
	
	// Processamento de Dados
	enquanto((num1 + num2) != 2){
		se((num1 % aux == 0) ou (num2 % aux == 0)){
			se(num1 % aux == 0){
				num1 = num1/aux
				}
			se(num2 % aux == 0){
				num2 = num2/aux
				}
			mmc = mmc * aux
				
		}senao{
			aux = aux + 1
			}
		}
	//Imprime na tela o resultado
	escreva("O M.M.C Entre ",num_1_antigo, " e ", num_2_antigo, " é: ", mmc)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 76; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */