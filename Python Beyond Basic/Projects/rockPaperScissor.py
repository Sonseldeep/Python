import random
class Game:
  def __init__(self):
    self.computer_pick = self.get_computer_pick()
    self.user_pick = self.get_user_pick()
    self.result = self.get_result()
    
  def get_computer_pick(self):
    random_number = random.randint(1,3)
    options = { 1: 'rock',2: 'paper',3:'scissors'}
    return options[random_number]
  
  def get_user_pick(self):
    while True:
      user_pick = input('Enter rock/paper/scissors')
      if user_pick in ('rock', 'paper', 'scissors'):
        break
      else:
        print("wrong input")
    return user_pick
  
  def get_result(self):
    if self.computer_pick == self.user_pick:
      return 'draw'
    elif self.user_pick == 'paper' and self.computer_pick == 'rock':
      return 'win'
    elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
      return 'win'
    elif self.user_pick == 'scissors' and self.computer_pick == 'rock':
      return 'win'
    else:
      return 'loss'
    
  def print_result(self):
    print(f"computer pick: {self.computer_pick}, computer pick: {self.computer_pick}")
    print(f'Your pick: {self.user_pick}')
    print(f'You {self.result}')
while True:
  game = Game()
  game.print_result()
  play_again = input("do you want to play again: ")
  if play_again !='y':
    break
    
