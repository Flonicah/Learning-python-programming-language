#building a guessing games in python
#creating the secret word store
print("The word Guessing Game")
print()
secret_word = "giraffe"

#creating a variable that will store the users response

guess = ""
#prompting the user to enter the guess again and again using the while loop for guessing

#while guess != secret_word:
 #   guess = input("Enter guess: ")
    
#print()
#print("Wow! you win")

#seting a limit for guessing the word three time
guess_count = 0#keeps tract of guess the user is guessing

# increment the guess count

guess_count =0

# setting guess limit

guess_limit = 3

# guess cases
out_of_guesses = False


while guess != secret_word and not (out_of_guesses):
    if guess_count< guess_limit:# checks the guest count
        guess = input("Enter guess: ")
        guess_count +=1
    else:
        out_of_guesses = True
    
    
if out_of_guesses:
    print("You are out of guesses . YOU LOSE")
else:
    print("WOW!,You win !")

 
