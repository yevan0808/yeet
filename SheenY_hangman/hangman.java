/*
Yevan Sheen
March 10,2020
Hangman Game
*/
import java.io.*;
import java.util.*;
public class hangman{
	static int score = 0;
	static int highscore = 0;
	static Scanner in = new Scanner(System.in);
	public static void main(String []args)throws Exception{
	welcome();
	gameMenu();
	}
	public static void welcome(){
		System.out.println("Welcome to my game! Have fun playing this hangman game and good luck!");
	}
	public static void gameMenu()throws Exception{
	boolean z = false;
	String input = "";
	String secretWord = "";
	while (z==false){
	System.out.println("Choose your category");
	System.out.println("Enter 1 for vegetables");
	System.out.println("Enter 2 for fruits");
	System.out.println("Enter 3 for fish");
	System.out.println("Enter 4 for instructions");
	System.out.println("Enter 5 for high score");
	System.out.println("Enter 6 to exit");
	input = in.nextLine();
	
	
	if (input.equals("1") || input.equals("2") || input.equals("3") || input.equals("4") || input.equals("5") || input.equals("6"))
		z = true;
	else
		System.out.println("invalid input");

	}
	
	
	//Gets the genre
	if (input.equals("1")){
		getVegetable();
		secretWord = getVegetable().trim();
	}
	else if (input.equals("2")){
		getFruit();
		secretWord = getFruit().trim();
	}
	else if (input.equals("3")){
		getFish();
		secretWord = getFish().trim();
	}
	else if (input.equals("4"))
		instructions();

	if (input.equals("5"))
		highScore1();
	if (input.equals("1")||input.equals("2")||input.equals("3"))
		hangman(secretWord);
	
	}
	//vegetables
	public static String getVegetable()throws Exception{
		String vegetable = "";
		Scanner scFile = new Scanner(new File("getVegetable.txt"));
		int vegetable1 =(int)(Math.random()*15)+1;
		for (int i = 1; i<=vegetable1;i++){
			vegetable = scFile.nextLine();
		}
	return vegetable;
	}
	//fruits
	public static String getFruit()throws Exception{
		String fruit = "";
		Scanner scFile1 = new Scanner(new File("getFruit.txt"));
		int fruit1 =(int)(Math.random()*40)+1;
		for (int i = 1; i<=fruit1;i++){
			fruit = scFile1.nextLine();
		}
	return fruit;
	
  
	}
	//fish
	public static String getFish()throws Exception{
		String fish = "";
		Scanner scFile = new Scanner(new File("getFish.txt"));
		int fish1 =(int)(Math.random()*22)+1;
		for (int i = 0; i<fish1;i++){
			fish = scFile.nextLine();
		}
	return fish;
	}
	//instructions
	public static void instructions()throws Exception{
		System.out.println("Options 1 2 and 3 will give you a random word from its category");
		System.out.println("Option 5 will give you your high score");
		System.out.println("Option 6 will exit you from the game");
		System.out.println("You have 5 lives");
		System.out.println("Please enter 1 character at a time unless using superguess");
		System.out.println("Please don't enter any numbers or special characters unless requested to do so");
		System.out.println("Most importantly, have fun!");
		System.out.println("");
		gameMenu();
	}
	//exit
	public static void exit(){
		System.exit(0);
	}
	//highscore
	public static void highScore1()throws Exception{
		
		System.out.println("Your high score is: "+highscore);
		gameMenu();
	}

	
	
	//Actual game
	public static void hangman(String str)throws Exception{
	int lives = 5;
	Scanner input = new Scanner(System.in);
	String guess = "";
	String underscore = "_ ";
	String hiddenWord = "";
	String badLetters = "";
	String code = "8";
	String superGuess = "";
	for (int i = 0; i<str.length()*0.5;i++){
		hiddenWord += underscore;
	}
		hiddenWord = hiddenWord.trim();
	
	System.out.println();
	System.out.println("Enter letters");
	
	
	
	while (lives > 0){
		boolean x = false;
		System.out.println("Your Secret Word: "+hiddenWord);
		System.out.println("Incorrect Letters: "+ badLetters);
		System.out.println("Your Score: " + score);
		System.out.println("Your lives: " + lives);
		System.out.println("ENTER superguess TO GUESS THE ENTIRE WORD");
		System.out.println("Instructions for superguess: You need to put a space between every letter and no spaces after writing out the entire word");
		//System.out.println(str);
		guess = input.nextLine();
		for (int i = 0; i<str.length();i++){  
			String y = str.charAt(i)+"";
			if (y.equals(guess.toLowerCase())){
				x = true;
				hiddenWord = hiddenWord.substring(0,i) + guess.toLowerCase()+ hiddenWord.substring(i+1);
			}
		}
		
	//Superguess
			if (guess.equals("superguess")){
				System.out.println("You have one try to guess the entire word");
				superGuess = input.nextLine();
				if (superGuess.equals(str)){
					System.out.println("You're correct!");
					score++;
					if (score>highscore){
						highscore = score;
					}
					gameMenu();
				}
				else{
					System.out.println("INCORRECT YOU LOSE");
					if (score>highscore){
						highscore = score;
						score = 0;
					}
					boolean playAgain1 = false;
					while (playAgain1 == false){
					System.out.println("Do you want to play again?");
					System.out.println("1. Yes");
					System.out.println("2. No");
					String playAgain = input.nextLine();
					if (playAgain.toLowerCase().equals("yes") || playAgain.equals("1")){
						score = 0;
						gameMenu();
						playAgain1 = true;
					}
					if (playAgain.toLowerCase().equals("no") || playAgain.equals("2")){
						playAgain1 = true;
						exit();
					}
					else
						System.out.println("Invalid input");
					}
				}
				
			}
		//bulletproof
		else if (guess.charAt(0)< 'a' || guess.charAt(0) > 'z'||guess.length()>1)
			System.out.println("invalid input");
		  
		//Checks if guess is incorrect
		else if (x == false && badLetters.indexOf(guess)==-1){
			badLetters += guess;
			lives--;
		}

				
		
		//Points  
		else if(str.equals(hiddenWord)){
			System.out.println(str);
			score++;
			System.out.println("Score: "+score);
			lives = 5;
			if (score>highscore){
				highscore = score;
			}
			gameMenu();
		}

		
	}
	//when you finish your word
	if (lives == 0){
		if (score>highscore){
			highscore = score;
			score = 0;
		}
		boolean playAgain1 = false;
			while (playAgain1 == false){
				System.out.println("Do you want to play again?");
				System.out.println("1. Yes");
				System.out.println("2. No");
				String playAgain = input.nextLine();
				if (playAgain.toLowerCase().equals("yes") || playAgain.equals("1")){
					score = 0;
					gameMenu();
					playAgain1 = true;
				}
				if (playAgain.toLowerCase().equals("no") || playAgain.equals("2")){
					playAgain1 = true;
					exit();
				}
				else
					System.out.println("Invalid input");
				}
	}   
	}






}