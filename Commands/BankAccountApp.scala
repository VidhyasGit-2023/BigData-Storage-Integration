/*Scala program to create a Bank Account App 
to monitor the transaction activities like deposit and withdraw etc.*/

class BankAccount(val accountNumber: String, var balance: Double) {
//function definition to monitor the deposit
  def deposit(amount: Double): Unit = {
    balance += amount
    println(s"Deposited $amount. New balance: $balance")
  }
//function definition to monitor the withdraw
  def withdraw(amount: Double): Unit = {
    if (amount <= balance) {
      balance -= amount
      println(s"Withdrew $amount. New balance: $balance")
    }else{
      println("Want to withdraw $amount? Insufficient balance!")
    }
  }
}

object BankAccountApp {
  def main(args: Array[String]): Unit = {
    //Class initialization
    val account = new BankAccount("VV-1234", 1000.0)
    println(s"Account Number: ${account.accountNumber}")
    println(s"Initial Balance: ${account.balance}")
    //function calling
    account.deposit(500.0)
    account.withdraw(200.0)
    account.withdraw(2000.0)
  }
}