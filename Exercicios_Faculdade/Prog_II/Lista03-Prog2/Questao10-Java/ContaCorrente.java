public class ContaCorrente
{
  private String conta;
  private double saldo;

  public ContaCorrente(String numConta, double saldoConta)
  {
    this.conta = numConta;
    this.saldo = saldoConta;
  } 	

  public void creditar(double valor)
  {
    this.saldo = saldo+valor;
  }
  
  public void debitar(double valor)
  {
    if (this.saldo >= valor)
    {
      this.saldo = this.saldo - valor;
    }
  }

  public double getSaldo()
  {
   return this.saldo;
  }
  
  public String getConta()
  {
     return this.conta;
  }

  public void setConta(String numConta)
  {
    this.conta = numConta;
  }

  public void setSaldo(double saldoConta)
  {
    this.saldo = saldoConta;
  }
}

