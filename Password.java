
import java.util.Scanner;
public class Password{
public static void main(String args[]){
Scanner sc = new Scanner(System.in);
System.out.print("Please enter your password: ");
String guess = sc.nextLine();
if(guess.equals("q")){
System.out.println("Correct, good job");
}else{
System.out.println("Incorrect Try Agian");
}

}
}
