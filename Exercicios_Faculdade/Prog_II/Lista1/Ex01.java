/*

1) Ler dois valores inteiros e apresentar sua: SOMA=xx, DIFERENÇA=xx, PRODUTO=xx, e MÉDIA=xx.

 */
package javaapplication3;
import java.util.Scanner;
/**
 *
 * @author Kurumi
 */
public class Ex01 {
        public static void main(String[] args) {
        // TODO code application logic here
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
            System.out.println("Digite o primeiro numero inteiro: ");
            int n1 = myObj.nextInt();  // Read user input
            
            System.out.println("Digite o segundo numero inteiro: ");
            int n2 = myObj.nextInt();  // Read user input
            
            System.out.println(n1+" + "+n2+" = " + (n1+n2) );  // Output user input
            System.out.println(n1+" - "+n2+" = " + (n1-n2) );  // Output user input
            System.out.println(n1+" * "+n2+" = " + (n1*n2) );  // Output user input
            System.out.println("("+n1+" + "+n2+")/2"+" = " + ((n1+n2)/2) );  // Output user input
        
    }
}
