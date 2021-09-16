// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 3) Crie um algoritmo que leia três lados de um triângulo e determine se ele é equilátero,
// isósceles ou escaleno. Quando os três lados forem iguais trata-se de um triângulo equilátero,
// dois lados iguais é um triângulo isósceles e os três lados diferentes é um triângulo escaleno.

programa
{
	
	funcao inicio()
	{
		// Declaração de Variáveis
		real lado1, lado2, lado3

		// Entrada dos Valores por parte do usuário
		escreva("Insira o lado 1 do triângulo: ")
		leia(lado1)
		
		escreva("Insira o lado 2 do triângulo: ")
		leia(lado2)
		
		escreva("Insira o lado 3 do triângulo: ")
		leia(lado3)

		// Verificação e Impressão dos Dados :

		// Verificação dos lados ( Equilátero )
		se(lado1 == lado2 e lado1 == lado3 e lado2 == lado3){
			escreva("Ele possui todos os Lados iguais, então ele é um triângulo Equilátero! ")
			}

		// Verificação dos lados ( Escaleno )
		senao se(lado1 != lado2 e lado1 != lado3 e lado2 != lado3){
			escreva("Ele possui todos os lados diferentes, então ele é um triângulo Escaleno")
			}

		// Verificação dos lados ( Isósceles )
		senao se( (lado1 == lado2 e lado1 != lado3) ou (lado2 == lado3 e lado2 != lado1) ) {
			escreva("Ele possui dois lados iguais e um diferente, então ele é um triângulo Isósceles")
			}

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 71; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */