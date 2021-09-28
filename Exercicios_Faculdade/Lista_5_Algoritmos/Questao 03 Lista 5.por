// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// 3) Escreva um algoritmo em PORTUGOL que determine se dois valores inteiros e positivos
// A e B são primos entre si. (dois números inteiros são ditos primos entre si, caso não
// exista divisor comum aos dois números)

programa
{
	
	funcao inicio()
	{
	// Declaração de variáveis
	inteiro A, B, dividendo, divisor, resto, mdc

	escreva("Programa Verificador de Número Primos entre si\n")
	// Entrada dos Valores por parte do usuário

	escreva("Digite o valor de A (número inteiro): ")
	leia(A)
	escreva("Digite o valor de B (número inteiro): ")
	leia(B)

	// Algoritmo para Verificar se dois números são Primos entre si
	// Ele cálcula se existe divisores comums entre os dois números,
	// Se houver MAIS DO QUE 1, os números não são primos entre si!
	se(A > B){
		dividendo = A
		divisor = B
	}
	senao{
		dividendo = B
		divisor = A
		}

	faca{
		resto = dividendo % divisor
		se (resto != 0){
			dividendo = divisor
			divisor = resto
			}
	}enquanto(resto!=0)

	mdc = divisor
	
	//Imprime na tela, se OS
	se(mdc == 1){
		escreva("A e B são primos entre si")
		}
	senao{
		escreva("A e B NÃO são primos entre si")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 920; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */