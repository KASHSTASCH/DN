import java.util.*;
public class Password_2{
	                public static void main(String args[]){
				Scanner sc = new Scanner(System.in);
				String PW = "fh";
				System.out.print("Enter your Password:  ");
				String Guess = sc.nextLine();
				if(Guess.equals(PW)){
					System.out.println("Correct, Nice");
				}else{
					    System.out.println("Incorrect, Try Again");
				}
			}
}
