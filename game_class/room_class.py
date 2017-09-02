
from game_class.monster_class import Monster



class Room():

	def __init__(self, room_number, num_of_monsters, monster_list):
		self._room_number = room_number
		self._num_of_monsters = num_of_monsters
		self._monster_list = monster_list
		self.list = []
		self.name = " "		

	
	@property	
	def room_number(self):
		return self._room_number



	@property 
	def num_of_monsters(self):
		return self._num_of_monsters


	@property
	def monster_list(self):
		print("In monster_list")
		print(self._num_of_monsters)
		for i in range(self._num_of_monsters):
			#self._monster_list[i]
			self.list.append(self._monster_list[i])
			print(self.list[i].name)
		#return ' '.join(self.list)
	
	
	def get_index_size(self, index):
		for i in range(self._num_of_monsters):
			self.list.append(self._monster_list[i])
		return(self.list[index].size)
	

	#@monster_list.setter
	def monster_pop(self):
		(self.list).pop(0)
		(self._monster_list).pop(0)
		self._num_of_monsters -= 1
		#return(self.list)
	
	def room_description(self, x):
		file = "./game_stories/room_stories.txt"
		lis = []
		listoflists = []
		i = 0
		new_line = ""
		with open(file, 'r') as infile:
			for line in infile:
				#print(line)
				if(line == " "):
					continue
				#print("Before split")
				lis = line.split()
				print(lis[0])
				print("This is x %s" %x)

				if(lis[0] == str(x)):
					print("Debug 2")
			#	if((lis[0] != None) and (lis[0] == str(x)):
			#		print("Debug")
				if(lis[0] != None and lis[0] == str(x)):
					print("got the line")
					listoflists.append(lis)
					new_line = line[2:]

		return(new_line)
		#file is a string that you will use to open the file
		
	#def 
		#pass



if __name__ == "__main__":
	#monster = ["bill", "gill", "tom"]
	monster_list = []
	for x in range(2):
		monster = Monster("a", 1, 1, "a")
		print("Your monster information")
		monster.name, monster.hp, monster.max_hp, monster.size = input().split(" ")
		monster_list.append(monster)
	print("The lenght is %s" %len(monster_list))
	room1 = Room(1, 2, monster_list)
	print(room1.room_number)
	print(room1.room_description(1))
	print(room1.monster_list)
	room1.monster_pop()
	print(room1.monster_list)
	
