// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 1) Dado o seguinte algoritmo, reescreva utilizando estrutura de repetição ENQUANTO, 
// de modo que produza a mesma saída (PSEUDO ou PORTUGOL).

// algoritmo fatoriais

// var 
// fat : real
// i,num : inteiro

// inicio
// Para num de 1 ate 10 faca

	// fat ← 1
	//   para i de 1 ate num faca
	//     fat ← fat*i

	// fim_para
	
	// escreva(“fatorial de”, num,”: “,fat)

// fim_para

// Fim

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	real fat
	inteiro i, num

	// Entra em uma repetição para calcular o fatorial de 1 ate 10
	para(num=1; num <= 10 ; num++){
		fat = 1
			// Calcula o Fatorial (fat) de um número específico (i)
			para(i=1; i<= num; i++){
				fat = fat * i
				}
		//Imprime na tela o  número digitado e o dia associado ao número.
		escreva("O Fatorial de ", num, ": ", fat, "\n")
		}
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 265; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */