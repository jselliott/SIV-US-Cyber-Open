#include <stdio.h>
#include <stdlib.h>
int gameSelection(int num)
{
	printf("Please select one of the following options:\n");
        printf("1. Play hangman with preloaded options\n");
        printf("2. Enter unique word and play hangman\n");
        printf("3. Exit\n");

	scanf("%d", &num);

	return num;
}

void playHangman(char word[])
{
	// Clear screen
	// Implement hangman game play. 
	printf("The word is %s.\n", word);
}

int main()
{
	// Implement 2D array to have more than one word to guess
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	char word[64] = "pwn";
	int num;

        printf("***IMPORTANT***\n");
        printf("This program is still a shell, code is still in development\n");
        printf("A full game of hangman is unavailable at this time\n\n");

	printf("Welcome to hangman v0.1!\n");
	num = gameSelection(num);
	if(num == 1)
	{
		playHangman(word);
	}
	else if(num == 2)
	{
		printf("Please enter a word: ");
		scanf("%s", &word);
		playHangman(word);
	}
	else if (num == 3)
	{
		printf("Thanks for playing!\n");
	}
	else
	{
		printf("Not a valid input.\n");
	}
	return 0;
}
