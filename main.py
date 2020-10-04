from random import randint

guess_number = randint(0, 20)
tries = 6
print ('Lets play a game of guess the number. What is your name?')
name = input ('')
print ('Lets Go ' + name)

while True:
  player_number = int(input(f'You have {tries} tries.\nGuess the number:\n'))

  if player_number == guess_number:
    print('Congratulations, you guessed the number!')
    break
  elif player_number > guess_number:
    print('Your guess is too high!')
    
  elif player_number < guess_number:
    print('Your guess is too low!')

  tries -= 1
  if tries <= 0:
    print("Sorry, but you didn't manage to guess the number")
    
    break
