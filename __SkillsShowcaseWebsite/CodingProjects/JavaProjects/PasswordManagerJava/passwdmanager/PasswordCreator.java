import java.util.Random;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.*; //https://chortle.ccsu.edu/java5/Notes/chap54/ch54_11.html
public class PasswordCreator {
                public static void main(String[] args){
                boolean go = true;
                boolean uPut = true;
                if(go = true){
                        Scanner in = new Scanner(System.in);
                        System.out.println("Welcome to the password generator function.  Next you will answer questions to determine the amount of letters, numbers, and symbols you want in your password.\n\tYour answers must:\n\t\t1.)Add up to a minimum of 8 character.\n\t\t2.)Must have at least 1 capital letter.\n\t\t3.)Must have at least 1 number.\n\t\t4.)Must have at least 1 special character.\n\tType 'quit' to quit program.");
                        System.out.println("Do you wish to continue? y/n ('y' starts program. 'n' quits the program.)");
                        String start= in.nextLine();
                        if (start.equals("y")){
                               uPut = true;
                        }
                        else if(start.equals("quit") || start.equals("Quit") || start.equals("n") || start.equals("N")){ //Scans for if the user wants to quit at this point in the program. If so it terminates the function.
                                System.out.println("Goodbye.");
                                //go = false;
                                return; //https://stackoverflow.com/questions/22452930/terminating-a-java-program
                        }
                        else{
                                System.out.println("Unrecognized input, restarting.");
                                uPut = false;
                        }
                        while(uPut = true){
                                System.out.println("Now, I need to ask you what the password is being used for?");
                                String category = in.nextLine();
                                if(category.equals("quit") || category.equals("Quit")){ //Scans for if the user wants to quit at this point in the program. If so it terminates the function.
                                        System.out.println("Goodbye.");
                                        return;
                                }
                                else if(uPut = true){//acts as an extra safety barrier so if a false is triggered inside this else if statement, the program has to skip to the end of the program and restart.
                                        //This section takes in the users requested amount of lowercase letters, goes through "safety checkpoints" to protect against code breaks, and manipulates the data for processing.
                                        System.out.println("Next, how many lowercase letters? (must be written as an be integer)");
                                        String lowCase = in.nextLine();
                                        if(lowCase.equals("quit") || lowCase.equals("Quit")){ //Scans for if the user wants to quit at this point in the program. If so it terminates the function. 
                                                System.out.println("Goodbye.");
                                                return;
                                        }
                                        try{ //try and except function to make sure the user input their request correctly, and restarts the program if it is not.
                                                int l = Integer.parseInt(lowCase);
                                        }
                                        catch(Exception e){
                                                System.out.println("Unrecognized input, restarting."); 
                                                uPut = false; //stops the inner while loop, causing the program to loop back to the first one, effectively "restarting" the program.
                                        }
                                        int l = Integer.parseInt(lowCase);
                                        //This section takes in the users requested amount of capital letters, goes through "safety checkpoints" to protect against code breaks, and manipulates the data for processing.
                                        System.out.println("How many Capital Letters?");
                                        String highCase = in.nextLine();
                                        if(highCase.equals("quit") || highCase.equals("Quit")){ //Scans for if the user wants to quit at this point in the program. If so it terminates the function.
                                                System.out.println("Goodbye.");
                                                return;
                                        }
                                        try{ //try and except function to make sure the user input their request correctly, and restarts the program if it is not.
                                                int h = Integer.parseInt(highCase);     
                                        }
                                        catch(Exception e){
                                                System.out.println("Invalid input, restarting.");
                                                uPut = false; 
                                        }
                                        int h = Integer.parseInt(highCase);
                                        if(h < 1){ //restarts the program if the user doesn't unclude at least 1 Capital Letter.
                                                System.out.println("You must have at least 1 capital letter, restarting.");
                                                uPut = false;
                                        }
                                        //This section takes in the users requested amount of numbers, goes through "safety checkpoints" to protect against code breaks, and manipulates the data for processing.
                                        System.out.println("How many numbers?");
                                        String numbers = in.nextLine();
                                        if(numbers.equals("quit") || numbers.equals("Quit")){ //Scans for if the user wants to quit at this point in the program. If so it terminates the function.
                                                System.out.println("Goodbye.");
                                                return;
                                        }
                                        try{ //try and except function to make sure the user input their request correctly, and restarts the program if it is not.
                                                int n = Integer.parseInt(numbers);        
                                        }
                                        catch(Exception e){
                                                System.out.println("Invalid input, restarting.");
                                                uPut = false;  //stops the inner while loop, causing the program to loop back to the first one, effectively "restarting" the program.
                                        }
                                        int n = Integer.parseInt(numbers);
                                        if(n < 1){ //restarts the program if the user doesn't unclude at least 1 number.
                                                System.out.println("You must have at least one number, restarting");
                                                uPut =false;
                                        }
                                        

                                        //This section takes in the users requested amount of special characters, goes through "safety checkpoints" to protect against code breaks, and manipulates the data for processing.
                                        System.out.println("Special Characters?");
                                        String specialChar = in.nextLine();
                                        if(specialChar.equals("quit") || specialChar.equals("Quit")){ //Scans for if the user wants to quit at this point in the program. If so it terminates the function.
                                                System.out.println("Goodbye.");
                                                return;
                                        }
                                        try{ //try and except function to make sure the user input their request correctly, and restarts the program if it is not.
                                                int s = Integer.parseInt(specialChar);   
                                        }
                                        catch(Exception e){
                                                System.out.println("Invalid input, restarting.");
                                                uPut = false; //stops the inner while loop, causing the program to loop back to the first one, effectively "restarting" the program.
                                        }
                                        int s = Integer.parseInt(specialChar);
                                        if(s < 1){
                                                System.out.println("You must include at least one special character in your password, restarting.");
                                                uPut =false;
                                        }
                                        if(l+h+n+s>=8 & uPut == true){ //if statement that acta like a safety checkpoint to protect against errors.
                                                //Ascii values from: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
                                                ArrayList<String> charList = new ArrayList<String>();//https://www.tutorialspoint.com/java/util/arraylist_add_index.htm
                                                for(int i=0;i<l;i++){
                                                        int lVal = new Random().nextInt(25+1) + 97 ;//https://mkyong.com/java/java-generate-random-integers-in-a-range/
                                                        char newLC = (char)(lVal); //https://www.codegrepper.com/code-examples/java/java+random+char+a-z
                                                        String newLow = String.valueOf(newLC);//https://www.javatpoint.com/java-char-to-string
                                                        charList.add(newLow);//https://www.tutorialspoint.com/java/util/arraylist_add_index.htm
                                                }
                                                //for loop that chooses a random Capital Letter and adds it to the charList
                                                for(int i=0;i<h;i++){
                                                        int hVal = new Random().nextInt(25+1) + 65; //selects ascii value of character
                                                        char newHC = (char)(hVal); // creates a char varibale with that value.
                                                        String newHigh = String.valueOf(newHC); //Converts that char value to a string.
                                                        charList.add(newHigh); //Adds it to the charList
                                                }
                                                //for loop that chooses a random number and add it to the charList.
                                                for(int i=0;i<n;i++){
                                                        int nVal = new Random().nextInt(10) + 47;
                                                        char newN = (char)(nVal); 
                                                        String newNum = String.valueOf(newN);
                                                        charList.add(newNum);
                                                }
                                                //for loop that chooses a random special character and adds it to the charList
                                                for(int i=0;i<s;i++){
                                                        int choose = new Random().nextInt(5); //first random selector to pick which group of special characters it will choose from.
                                                        if(choose == 0){
                                                                int sVal = 33; // ascii value for the '!'.
                                                                char newSC = (char)sVal; 
                                                                String newSpec = String.valueOf(newSC);
                                                                charList.add(newSpec);
                                                        }
                                                        else if(choose == 1){
                                                                int sVal = new Random().nextInt(4) + 34; //second selector for the ascii values 35 - 38 (#,$,%,&)
                                                                char newSC = (char)(sVal); //sets a char variable with the same value.
                                                                String newSpec = String.valueOf(newSC);//converts that char variable to a string.
                                                                charList.add(newSpec);//adds that new character to the charList
                                                        }
                                                        else if(choose == 2){
                                                                int sVal = 42; //ascii value for the '*'
                                                                char newSC = (char)(sVal); 
                                                                String newSpec = String.valueOf(newSC);
                                                                charList.add(newSpec);
                                                        }
                                                        else if(choose == 3){
                                                                int sVal = 64; //ascii value for the '@'
                                                                char newSC = (char)(sVal); 
                                                                String newSpec = String.valueOf(newSC);
                                                                charList.add(newSpec);
                                                        }
                                                        else if(choose == 4){
                                                                int sVal = 94; //ascii value for the '^'
                                                                char newSC = (char)(sVal); 
                                                                String newSpec = String.valueOf(newSC);
                                                                charList.add(newSpec);
                                                        } 
                                                }       
                                                //Function used in the next four lines: https://stackoverflow.com/questions/13695547/arraylist-of-strings-to-one-single-string
                                                StringBuilder passwordBuilder = new StringBuilder(); //Creates a string builder that acts like an arraylist, but justs adds the characters together instead of keeping them seperate.
                                                for (String p : charList) { //for each loop that goes through the charlist
                                                        passwordBuilder.append(p).append(""); //appends each index of the charList to the new string.
                                                }
                                                
                                                //These next three lines create a list for passwords and save the new one to it.
                                                ArrayList<String> passwordList = new ArrayList<String>(); //new arrayList to hold created passwords while the program is running.
                                                String newPassword = passwordBuilder.toString(); //sets the password builder as a new variable for the next step.
                                                passwordList.add(newPassword); //adds the newPassword to a temporary list of passwords, for the database.
                                                Scanner sc = new Scanner(System.in);
                                                System.out.println("\nThe password for " +category+ " is: " +newPassword);
                                                System.out.println("\n\nWould you like to run this program again? (y/n)\n");
                                                String repeat = sc.nextLine();
                                                if(repeat.equals("n") || repeat.equals("quit") || repeat.equals("Quit")){
                                                        return;
                                                }   
                                        }
                                        else{
                                                System.out.println("Password length is too short, restarting data collection.");
                                        }
                                }
                                else{
                                        System.out.println("Incorrect input, please try again");    
                                } 
                        }
                }
        }
}
