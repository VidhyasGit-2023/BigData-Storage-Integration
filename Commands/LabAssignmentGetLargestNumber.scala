/*Scala program to create a user-defined function 
to return largest number among two numbers.*/

object LabAssignmentGetLargestNumber {
    //function definition to get the largest number
    def getLargestNumber(num1: Int, num2: Int) : Int ={
        var largestNumber: Int=0;
        if(num1 > num2)
            largestNumber=num1;
        else
            largestNumber=num2;
        
        return largestNumber;
    }
    
    def main(args: Array[String]): Unit = {
        var Number1: Int=17638;
        var Number2: Int=17683;
        
        //function calling
        println("Largest number from "+ Number1+" and "+ Number2 +" is: "+ getLargestNumber(Number1,Number2));
        
    }
}