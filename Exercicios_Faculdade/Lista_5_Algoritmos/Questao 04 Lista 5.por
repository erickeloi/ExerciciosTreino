// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 4) Escreva um algoritmo em PORTUGOL que:

//  -leia 100 fichas, onde cada ficha contém o número de matrícula e a nota de
//cada aluno de um determinado curso;

// -Determine e imprima as duas maiores notas, juntamente com o número de
//matrícula do aluno que obteve cada uma delas;

// -Suponha que não exista dois ou mais alunos com a mesma nota.

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis

	// Mudando o "total_alunos" você deixa altera o número de Inputs/Alunos,
	// Podendo testar o programa de forma facilitada.
	
	// exemplo: total_alunos = 3
	const inteiro total_alunos = 100
	
	real notas_alunos[total_alunos], 
	maior = 0.0, menor = 0.0, maior2 = 0.0, aux
	
	inteiro matricula_alunos[total_alunos], contador,
	matricula_maior_nota = 0, matricula_maior_nota2 = 0, matricula_menor_nota = 0
	
	// Entrada dos Valores por parte do usuário + Processamento
	para(contador = 0; contador < total_alunos; contador++){
			escreva("Digite o número de matrícula do Aluno '", contador,"': ")
			leia(matricula_alunos[contador])
			
			escreva("Digite a 1ª nota do aluno '", contador, "': ")
			leia(aux)
			
			// Se esse for o primeiro loop,
			// A primeira nota é tanto a Maior nota Quanto a Menor nota.
			se(contador == 0){
				maior = aux
				menor = aux
				maior2 = aux
				
				matricula_maior_nota = matricula_alunos[contador]
				matricula_maior_nota2 = matricula_alunos[contador]
				matricula_menor_nota = matricula_alunos[contador]
				}
			// Se o valor digitado for MAIOR que a "MAIOR NOTA" registrada,
			// a Nova "Maior Nota" vai ser o valor digitado agora.
			senao se(aux > maior){
				// A Variavel maior2 vira o "maior" passado, assim como
				// A "matricula_maior_nota2" vira a "matricula_maior_nota" anterior.
				maior2 = maior
				matricula_maior_nota2 = matricula_maior_nota
				
				maior = aux
				matricula_maior_nota = matricula_alunos[contador]
				}
			// Se o valor digitado for MENOR que a "MENOR NOTA" registrada,
			// a Nova "Menor Nota" vai ser o valor digitado agora.
			senao se(aux < menor){
				menor = aux
				matricula_menor_nota = matricula_alunos[contador]
				}
				
			notas_alunos[contador] = aux
				
		}

	//Os Códigos abaixo Imprimem na tela os resultados...
	escreva("Exibindo na tela... \n")
	
	// Exibe o Aluno com a Maior Nota
	escreva("\nO aluno com número de matrícula '", matricula_maior_nota, "' Obteve a Maior Nota, de: ", maior)

	// Exibe o Aluno com a Segunda Maior Nota
	escreva("\nO aluno com número de matrícula '", matricula_maior_nota2, "' Obteve a Segunda Maior Nota, de: ", maior2)

	// Exibe o Aluno com a Menor Nota
	escreva("\nO aluno com número de matrícula '", matricula_menor_nota, "' Obteve a Menor Nota, de: ", menor)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1974; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */