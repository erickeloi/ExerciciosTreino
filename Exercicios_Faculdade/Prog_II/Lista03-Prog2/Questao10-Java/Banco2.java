// Aluno e Matricula:
// ERICK ELOI PIMENTA PIMENTEL
// 202111140012

// THIAGO AMORIM NUNES
// 201811140038

// Sinceramente, eu prefiro muito mais programar em Python,
// Porém, nada contra Java. (Exceto que ele é muito verboso e eu achei meio difícil o sistema de input)
// -Erick

import java.util.ArrayList;
import java.util.Scanner;

public class Banco2 {

    ArrayList<ContaCorrente> ContasCadastradas = new ArrayList<ContaCorrente>();

    void adicionaConta(ContaCorrente ContaCorrenteInput){
        // Verifica se o banco de dados encontra-se vazio
        if(!ContasCadastradas.isEmpty()){
            // Verifica se a conta já foi cadastrada no banco
            for(ContaCorrente ContaCorrenteBanco: ContasCadastradas){
                if(ContaCorrenteBanco.getConta().equals(ContaCorrenteInput.getConta())){
                    // Se a conta já foi cadastrada no banco, não adiciona uma nova
                    System.out.println("O Número de conta informado já existe no banco de dados...");
                    System.out.println("Operação Cancelada");
                    return;
                }
            }
            // Verifica se a conta ainda não foi cadastrada no banco, ele cadastra.
            ContasCadastradas.add(ContaCorrenteInput);
            System.out.println("conta adicionada com sucesso! ");

        }else{
            // Se não existirem contas cadastradas no banco, essa vai ser a primeira conta cadastrada.
            ContasCadastradas.add(ContaCorrenteInput);
            System.out.println("conta adicionada com sucesso! ");
        }
    }

        // Função que retorna uma Conta Vazia (Função Auxiliar)
        ContaCorrente Return_Null_Account(){
        ContaCorrente nullAccount = new ContaCorrente("null",0);
        return nullAccount;
        }

        // Procura se uma conta existe no banco, se não existir, retorna uma null account.
        ContaCorrente obterConta(String numero_conta){
        if(!ContasCadastradas.isEmpty()){
            Boolean ACCOUNT_FOUND = false;
            for(ContaCorrente Conta_Corrente: ContasCadastradas){
                if(Conta_Corrente.getConta().equals(numero_conta)){
                    ACCOUNT_FOUND = true;
                    return Conta_Corrente;
                }
            }
            if (ACCOUNT_FOUND == false){
                ContaCorrente nullAccount = Return_Null_Account();
                return nullAccount;
            }
        }else{
            ContaCorrente nullAccount = Return_Null_Account();
                return nullAccount;
        }
        ContaCorrente nullAccount = Return_Null_Account();
        return nullAccount;
    }

    // Função que remove uma conta especifica (Numero da Conta) do banco de dados.
    void removerConta(ContaCorrente ContaCorrenteInput){
        if(!(ContasCadastradas.isEmpty())){
            for(ContaCorrente ContaCorrenteBanco: ContasCadastradas){
                if(ContaCorrenteBanco.getConta().equals(ContaCorrenteInput.getConta())){
                    ContasCadastradas.remove(ContaCorrenteBanco);
                    System.out.println ("Conta removida com sucesso!");
                    break;
                }
            }
            System.out.println ("Conta não encontrada no banco de dados!");
        }else{
            System.out.println ("Sem contas cadastradas no Banco de dados!");
        }

    }

    // Função que exibe todas as contas cadastradas
    void exibirContas(){
        if(!(ContasCadastradas.isEmpty())){
            for(ContaCorrente Conta_Corrente: ContasCadastradas){
                System.out.println ("-------------------------------------");
                System.out.println ("Conta Corrente N° "+Conta_Corrente.getConta()+", Saldo: "+Conta_Corrente.getSaldo()+"R$");
                System.out.println ("-------------------------------------");

            }
        }else{
            System.out.println ("Sem contas cadastradas no Banco de dados!");
        }
    }

    Boolean isBancoVazio(){
        return ContasCadastradas.isEmpty();
    }

    public static void main(String[] args){
    
    // Instanciando a classe do Banco
    Banco2 Banco_Java = new Banco2();

    // Instanciando a variável de Opção e de Scanner 
    // Para acesso ao Menu
    int op;
    Scanner opcao = new Scanner(System.in); 

    // Menu do Banco
    do{
        System.out.println("Java Free Bank");
        System.out.println("1 - Cadastrar Conta Corrente");
        System.out.println("2 - Consultar Conta Corrente");
        System.out.println("3 - Exibir Contas Cadastradas");
        System.out.println("4 - Remover Conta Corrente");
        System.out.println("0 - Sair");

        System.out.println ("Sua Opção: ");
        op = opcao.nextInt();

        switch (op){
            case 1:
                Scanner input = new Scanner(System.in);
                System.out.println("Informe o Número da Conta Corrente: ");
                String numConta = input.nextLine();

                System.out.println("Informe o Saldo da Conta: ");
                double SaldoConta = input.nextDouble();
                ContaCorrente Conta_Corrente_aux = new ContaCorrente(numConta, SaldoConta);

                Banco_Java.adicionaConta(Conta_Corrente_aux);
                break;
            case 2:
                if (!Banco_Java.isBancoVazio()){
                    Scanner input2 = new Scanner(System.in);
                    System.out.println("Digite o Número da Conta Corrente que deseja Consultar: ");

                    String num_conta_aux = input2.nextLine();
                    ContaCorrente conta_aux = Banco_Java.obterConta(num_conta_aux);

                    if(conta_aux.getConta()=="null"){
                        System.out.println ("Conta não encontrada ou Instabilidade na conexão com o banco de dados");
                    }
                    else{
                        System.out.println ("-------------------------------------");
                        System.out.println ("Conta Corrente N° "+conta_aux.getConta()+", Saldo: "+conta_aux.getSaldo()+"R$");
                        System.out.println ("-------------------------------------");
                    
                    }
                    break;

                }
                else{
                    System.out.println ("Não existem contas Cadastradas no Banco Nesse momento");
                }
            case 3:
                Banco_Java.exibirContas();
                break;
            case 4:
            if (!Banco_Java.isBancoVazio()){
                Scanner input3 = new Scanner(System.in);
                System.out.println("Digite o Número da Conta Corrente que deseja Deletar: ");
                String searchAccount = input3.nextLine();

                ContaCorrente conta3 = new ContaCorrente(searchAccount,0.0);

                Banco_Java.removerConta(conta3);
                break;   
            }else{
                System.out.println ("Não existem contas Cadastradas no Banco Nesse momento");
            }

        }
    }while(op!=0);	
  }
}
