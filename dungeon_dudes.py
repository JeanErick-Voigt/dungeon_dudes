#! /usr/bin/env/ python3

import sys
from random import random
from game_class.room_class import Room
from game_class.monster_class import Monster
from game_class.player_class import Player



def get_monster(x):
	#function used to get the monsters from a text file
	file = "./game_stories/monsterfile.txt"
	lis = [] 
	listoflists = []
	i = 0
	new_line = ""
	with open(file, 'r') as infile:
		for line in infile:
			if(line == " "):
				continue
			lis = line.split()
			if(lis[0] != None and lis[0] == str(x)):
				new_line = line[2:]
				#print(new_line)
	#print(new_line)
	return(new_line.lstrip())


def random_choice():
	#function used to get a random number within the value
	x = 0
	while(x < 1):
		x = random()
		x = (int(x * 100) % 18)
	
	return(x)


def room_monsters(room_monster_count):
	#appends random monsters to a list to be placed for each room
	random_num = 0
	room_monster_list = []
	print("Room monsters function count {}".format(room_monster_count))
	for i in range(room_monster_count):
		monster = Monster("a", 1, 1, "a")
		random_num = random_choice()
		monster.name, monster.size =  get_monster(random_num).split(" ")
		set_initial_hp_values(monster)
		room_monster_list.append(monster)
	return(room_monster_list)
	

def set_initial_hp_values(monster):
	#designed to set the initial hp and max_hp values
	if "small" in monster.size:
		monster.hp = 1
		monster.max_hp = 1
	elif "medium" in monster.size:
		monster.hp = 2
		monster.max_hp = 2
	else:
		monster.hp = 3
		monster.max_hp = 3
	return(monster)
	

def initiative_roll():
	#takes the initiative roll in order to see who gets the first turn
	player_roll = random()
	player_roll = (int(player_roll * 100) % 6)
	player_roll += 1
	monster_roll = random()
	monster_roll = (int(monster_roll * 100) % 6)
	monster_roll += 1
	print("Roll for initiative...")
	print("You rolled a {0}, Monster rolled a {1}".format(player_roll, monster_roll))
	if(player_roll > monster_roll):
		print("You have won the initiative", end=" ")
		print("You may choose to attack")
		outcome = 1	
	else:
		print("you lost initiative and will be attacked")
		outcome = -1
	return(outcome)


def game_choice(winner, turn):
	#makes a game choice to select what you want to do
	print("please select from the following options")
	print("""1. Attack
2. RunAway
3. Check_loot
4. check_status
5. Use_item
6. Quit 
7. Restart
""")
	ans = " "
	select = 1
	while(select and turn == 1):
		ans = int(input())
		if(winner == -1 and ans == 1):
			print("You lost initiative and  can not attack first")
			print("Please, select another option")
		
		elif(int(ans) > 7 or int(ans) < 1):
			print("Did not select an appropiate option")
			continue
		else:
			select = 0
	if(turn > 1):
		ans = int(input())
	return(ans)

def turn_execution(choice):
	#executes the game choice
	my_turn = 1
	print("This is choice %s" %choice)
	while(my_turn):
		if(str(choice) == "1"):
			outcome = attack()
			print("This is outcome %s" %outcome)
			return(outcome)
			
		elif(str(choice) == "2"):
			pass
		elif(str(choice) == "3"):
			pass
		elif(choice == 4):
			pass
		elif(choice == 5):
			pass
		elif(choice == 6):
			pass
		elif(str(choice) == "7"):
			break

def welcome():
	#initial loop that initializes the name of the user to the program
	loop = 1
	print("Welcome to dungeons and dudes.")
	print("Please enter a name or quit to exit")
	while(loop):
		ans = input()
		if(len(ans) < 1):
			print("please re-enter a name or enter 'default' for a default name")
		elif(ans == "quit"):
			print("You have chosen to exit. Are you sure? y or no >")
			ans = input()
			if(ans == "y"):
				print("exiting...")
				sys.exit()
			else:
				print("please re-enter your name")
				continue
		elif(ans == "default"):
			ans = "Hero"
			break
		else:
			None
			loop = 0
		print("Is {} really the name you want to use? y or no?".format(ans))
		ans2 = input()
		if(ans2 == "y"):
			break
		else:
			continue

	print("Hello {}, welcome to the game".format(ans))
	return(ans)

def attack():
	#This is attack function.  
	size = current_room.get_index_size(0)
	print("This is size {}".format(size))
	rolls = 0
	print("This is rolls %s" %rolls)
	outcome = 0
	player_list = []
	monster_list = []
	if("large" in size):
		rolls = 3

	elif("medium" in size):
		rolls = 2

	else:
		rolls = 1

	for i in range(3):
		player_roll = int(random() * 100)
		player_roll = (player_roll %6) + 1		
		player_list.append(player_roll)
	for i in range(rolls):
		monster_roll = int(random() * 100)
		monster_roll = (player_roll %6) + 1
		monster_list.append(monster_roll)
	player_list.sort()
	monster_list.sort()
	print("player rolled {}".format(player_list))
	print("monster rolled {}".format(monster_list))
	if(rolls == 1):
		if(player_list[2] > monster_list[0]):
			outcome = 1
			if(current_room.list):
				return(-5)
			current_room.monster_pop()
		else:
			Hero.hp_hit()

	elif(rolls == 2):
		if(player_list[1] > monster_list[1]):
			if(current_room.list):
				return(-5)

			current_room.monster_pop()
		elif(player_list[2] <= monster_list[1]):
			Hero.hp_hit()
			Hero.hp_hit()
		elif(player_list[1] <= monster_list[1]):
			Hero.hp_hit()
			if(player_list[0] > monster_list[0]):
				outcome = -1
	
	else:
		if(player_list[0] > monster_list[0]):
			outcome -=1
		else:
			Hero.hp_hit()
		if(player_list[1] > monster_list[1]):
			outcome -=1
	
		else:
			Hero.hp_hit()
		if(player_list[2] > monster_list[2]):
			outcome -= 1
		else:
			Hero.hp_hit()
	print("End of attack function")
	return(outcome)			



def amount_of_monsters():
	#returns the amount of monsters
	num = int(random() * 100)
	num = (num % 4) + 1
	return(num)
		

if __name__ == "__main__":
	monster_list = []
	x = 0
	in_room = 0
	room_num = 0
	#player_name = welcome()
	Hero = Player("Bob", 10, 10) 
	while(room_num < 6):
		#in_room = 0
		in_room += 1
		turn = 0
		room_num += 1
		monster_number = amount_of_monsters()
		winner = (initiative_roll())
		outcome = 0
		while(in_room):
			turn += 1
			monster_list = room_monsters(monster_number)
			current_room = Room(room_num, monster_number, monster_list)
			print(current_room.room_description(room_num))
			#print(monster_list[0].name)
			#print(monster_list[0].size)
			#print(monster_list[0].hp)
			#print(monster_list[0].max_hp)
			#print(monster_list[1].name)
			#for i in range(monster_number):
			#	set_initial_hp_values(monster_list[i])

			menu_selection = game_choice(winner, turn)
			outcome += turn_execution(menu_selection)
			print(current_room.monster_list)
			if(current_room.get_index_size  == outcome):
				current_room.monster_pop()
			
			if(not current_room.monster_list):
				in_room = 0

	
	#random_num = random_choice()
	#room_monsters(monster_number
	'''while(x < 1):
		print("in while loop")
		x = random()
		x = (int(x * 100) % 18)

	
	print(x)
	
	monster1 = Monster("a", 1, 2, "sm")
	'''
	#x = (int(x * 100) % 18)
	'''print(x)
	'''
	#print(get_monster(x))	
	'''monster1.name, monster1.size = get_monster(x).split(" ")
	'''
	#print(monster1.name)
	#print(monster1.size)
	#print(len(monster1.size))
	#if(monster1.size == "small"):
	#	print("size is small")
	#set_initial_hp_values(monster1)
	#monster1.show_info()
	
	#while(game):
	#	room
