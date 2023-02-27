import java.util.Scanner;

public class Password_2{
public static void main(String args[]){
Scanner sc = new Scanner(System.in);
	System.out.print("Enter your password: ");
String guess = sc.nextLine();
if(guess.equals("fh")){
System.out.println("Correct");
}else{
System.out.println("Incorrect");
}
}

}
