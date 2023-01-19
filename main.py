import random

count = 1

num = random.randint (0,5)

guess = num



while count != 12:

  
  
 

  guess = int(input('Guess number between 1 - 5:'))
  count += 1

  if guess == num:

    print ("you got it you win!")
    break
  elif guess < num:

    print ("Too Low")

  elif guess > num:

    print("Too High.")
  
  elif count == 10:
    print ("You lose")
  
  else:

    print("That's not a number. Try again.")

    continue





 
