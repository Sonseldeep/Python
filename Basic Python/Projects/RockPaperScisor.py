print('---------------------------------')
import random

def computer_choice():
  
  randomNumber = random.randint(1,3 )
  options = { 1: 'rock',
             2:'paper',
             3:'scissor'}
  
  choice = options[randomNumber]
  return choice

def userInput():
  user = input("enter rock/paper/scissor: ")
  user = user.lower()
  return user


def winner(userDetails,computerDetails):
  if userDetails == computerDetails:
    return "draw"
  elif (userDetails=='rock' and computerDetails=='scissor'):
    return "win"
  elif (userDetails=='scissor' and computerDetails=='paper'):
    return 'win'
  elif (userDetails=='paper' and computerDetails=='rock'):
    return 'win'
  else:
    return 'loss'
  

userDetails = userInput()
computerDetails = computer_choice()
result=winner(userDetails,computerDetails)

print(f"computer: {computerDetails}")
print(f"your pick: {userDetails}")
print(f"result:{result}")

print('---------------------------------')