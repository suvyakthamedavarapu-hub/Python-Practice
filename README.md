# Python-
Number Guessing Game:
   It is a simple and fun console-based Python game designed for beginners.
   The program randomly generates a number, and the player has a limited number of attempts to guess it correctly.
Concepts Used:
  1) Random Module --> Used to generate a random number within a predefined range.
  2) Loops (While Loop) --> Used to control the number of chances given to the player.
  3) Conditional Statements (if–else) --> Used to check whether the guessed number is correct, too high, or too low.
  4) Print Statements --> Used to display messages indicating whether the user has won or failed.
Game Process:
  - The program generates a random number within a predefined range.
  - The user is given 5 chances to guess the number.
  - If the user guesses the correct number on the first attempt, the program displays a winning message and exits.
  - If the guess is incorrect, the program responds with:
  - “Too low” if the guessed number is less than the generated number.
  - “Too high” if the guessed number is greater than the generated number.
  - The game continues until:
       -> The user guesses the correct number within the given chances, or
       -> All chances are exhausted.
  - If the user fails to guess the number within the allowed attempts, the program displays a failure message along with the secret number.
Outcome:
  - Win: The user guesses the correct number within the given chances.
  - Lose: The user fails to guess the number within the allowed attempts.
