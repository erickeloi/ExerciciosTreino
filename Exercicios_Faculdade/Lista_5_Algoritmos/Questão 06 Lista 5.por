// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 6) Chico tem 1,50m e cresce 2 centímetros por ano, 
// enquanto Juca tem 1,10m e cresce 3 centímetros por ano. 

// Construir um algoritmo em PORTUGOL que calcule iterativamente
// e imprima quantos anos serão necessários para que Juca seja maior que Chico.

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	real altura_chico = 1.5, altura_juca = 1.1, 
	taxa_crescimento_chico = 0.02, taxa_crescimento_juca = 0.03

	inteiro contador_anos = 0, contador

	escreva("Atualmente, Chico tem : ", altura_chico," Metros de Altura, \n")
	escreva("Atualmente, Juca tem : ", altura_juca," Metros de Altura \n")
	
	escreva("Passaram-se 0 Ano(s) \n")
	
	// Processamento de Dados
	enquanto(altura_juca < altura_chico){
	altura_chico = altura_chico + (altura_chico * taxa_crescimento_chico)
	altura_juca = altura_juca + (altura_juca * taxa_crescimento_juca)
	
	contador_anos++

	escreva("Atualmente, Chico tem : ", altura_chico," Metros de Altura, \n")
	escreva("Atualmente, Juca tem : ", altura_juca," Metros de Altura \n")
	
	escreva("Passaram-se ", contador_anos, " Ano(s) \n\n")
	}
	
	//Imprime na tela o resultado final

	escreva("\nEntão, vão ser necessarios ", contador_anos, " Anos para que Juca seja Maior que Chico \n\n")
	escreva("Conclui-se que, Chico terá : ", altura_chico," Metros de Altura, \n")
	escreva("Conclui-se que, Juca terá : ", altura_juca," Metros de Altura \n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1154; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */