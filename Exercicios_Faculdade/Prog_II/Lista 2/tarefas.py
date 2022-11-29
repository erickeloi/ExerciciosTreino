# Prof.Lídio Mauro Lima de Campos
# Assunto: Herança, Classes Abstratas e Interfaces

# 1- Escreva a classe ObjetoGeometrico que represente um objeto geométrico em duas
# dimensões. Esta classe deve ter métodos para inicializar o objeto, mostrar seus dados e
# calcular e retornar a sua área e perímetro. Usando esta classe como base, escreva as
# classes herdeiras Circulo (contendo duas coordenadas para o centro e um raio),
# Retangulo (contendo dois valores para os lados) e Triangulo (contendo três valores para
# os lados), que sobrepõem os métodos descritos em ObjetoGeometrico. Dicas: a área de
# um círculo pode ser calculada com Math.PI*r*r, onde r é o raio do círculo. O perímetro
# de um círculo é dado por 2*Math.PI*r. A área do retângulo é dada por b*h onde b é um
# dos lados e h é o outro lado. Seu perímetro é dado por 2*b+2*h. A área de um triângulo
# é dada por Math.sqrt(s*(s-a)*(s-b)*(s-c)) onde Math.sqrt é a função que calcula a raiz
# quadrada, a, b e c são os lados do triângulo e s é a metade do perímetro do triângulo. O
# perímetro do triângulo é calculado como (a+b+c). Apresentar o diagrama UML, Fazer
# instâncias das classes herdeiras na classe principal, apresentando como saída áreas e
# perímetros dos objetos geométricos.


# 2- Usando o exercício 1 como base, escreva as classes Quadrado, que herda da classe
# Retangulo mas somente precisa inicializar um dos lados, e as classes
# TrianguloEquilatero, TrianguloIsosceles e TrianguloEscaleno que precisam inicializar
# somente um, dois ou três lados do triângulo. Para cada uma destas classes, quais
# métodos devem ser sobrepostos e quais podem ser aproveitados, apresentar Diagrama
# UML e Fazer instâncias das classes herdeiras na classe principal, apresentando como
# saída áreas e perímetros dos objetos geométricos.


# 3- Crie uma hierarquia de classes de domínio para uma loja que venda livros, CDs e
# DVDs. Sobrescreva o método toString() para que imprima:
# • Para livros: nome, preço e autor;
# • Para CDs: nome, preço e número de faixas;
# • Para DVDs: nome, preço e duração.

# Evite ao máximo repetição de código utilizando a palavra super no construtor e no
# método sobrescrito. Em seguida, crie uma classe Loja com o método main() que
# adicione 5 produtos diferentes (a sua escolha) a um vetor e, por fim, imprima o
# conteúdo do vetor. Apresentar o Diagrama UML.



# 4-Modifique o código do programa anterior, da seguinte forma:
# a) Adicione um atributo que represente o código de barras do produto (é um valor
# obrigatório e, portanto, deve ser pedido no construtor;
# b) Sobrescreva o método equals() retornando true se dois produtos possuem o mesmo
# código de barras;
# c) Na classe Loja, implemente um simples procedimento de busca que, dado um
# produto e um vetor de produtos, indique em que posição do vetor se encontra o produto
# especificado ou imprima que o mesmo não foi encontrado; 