import random
from art import logo
from art import vs
from game_data import data
from replit import clear

print(logo)
main_list = []
for i in range(0, 2):
  random_person = random.choice(data)
  main_list.append(random_person)	

score = 0
game_continue = True
while game_continue:
  while main_list[0] == main_list[1]:
    main_list.pop()
    main_list.append(random.choice(data))

  name_A = main_list[0]["name"]
  foll_A = main_list[0]["follower_count"]
  desc_A = main_list[0]["description"]
  country_A = main_list[0]["country"]
  #use .remove()
  name_B = main_list[1]["name"]
  foll_B = main_list[1]["follower_count"]
  desc_B = main_list[1]["description"]
  country_B = main_list[1]["country"]
  #debug
  print(f"A : {foll_A}")
  print(f"B : {foll_B}")
  
  
  print(f"Compare A: {name_A}, a {desc_A}, from {country_A}")
  print(vs)
  print(f"against B: {name_B}, a {desc_B}, from {country_B}")
  user = input("Who has more followers, A or B:  ").lower()
  if user == "a":
    if foll_A > foll_B:
      score += 1
      
      print(f"you are right. current score: {score}")
      main_list.pop(0)
      main_list.append(random.choice(data))
      clear()
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      game_continue = False
          
  elif user == "b":
    if foll_B > foll_A:
      score += 1
      print(f"you are right. current score: {score}")
      main_list.pop(0)
      main_list.append(random.choice(data))
      clear()
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      game_continue = False
