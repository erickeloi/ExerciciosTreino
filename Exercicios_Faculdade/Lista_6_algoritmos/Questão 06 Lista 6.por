// Aluno: Erick Eloi Pimenta Pimentel
// N° de matricula: 202111140012

// Ex.06
programa {
	funcao inicio() {
		real alturas_atletas[5][10],
		maiores_alturas[5], 
		maior_altura = 0.0
		
		inteiro c, cl,cc
		
		para(cl=0;cl<5;cl++){
			maior_altura = 0.0
			para(cc=0;cc<10;cc++){
		        escreva("Digite a Altura do Atleta Nº", cc, ", da Delegação ", cl,": ")
		        leia(alturas_atletas[cl][cc])
		        
		        se(cc == 0){
		        	maior_altura = alturas_atletas[cl][cc]
		        	}
		        senao se(alturas_atletas[cl][cc] > maior_altura){
		        	maior_altura = alturas_atletas[cl][cc]
		        	}
		        	
			}
			maiores_alturas[cl] = maior_altura
		}

		// Imprime na tela
		escreva("As Alturas dos atletas de cada delegação são: \n")
		para(cl=0;cl<5;cl++){
			escreva("Delegação ", cl,": \n")
			para(cc=0;cc<10;cc++){
				escreva(alturas_atletas[cl][cc], ", ")
			}
			escreva("\n")
		}

		
		escreva("As Maiores Alturas dos Atletas de cada Delegação: \n")
		para(c=0;c<5;c++){
			escreva("Delegação ",c,": ", maiores_alturas[c]," \n")
			}
			
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 959; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {alturas_atletas, 7, 7, 15}-{maiores_alturas, 8, 2, 15}-{maior_altura, 9, 2, 12};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */