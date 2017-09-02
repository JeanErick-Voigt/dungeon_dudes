from game_class.character_class import Character


class Monster(Character):
	def __init__(self, name, hp, max_hp, size):
		#self._name = name
		#self._hp = hp
		#self._max_hp = max_hp
		super().__init__(name, hp, max_hp)
		self._size = size


	@property
	# getter for size
	def size(self):
		return self._size


	@size.setter
	#setter for size
	def size(self, size):
		self._size = size
		#return self._size


if __name__ == "__main__":
	x = 5
	def get_monster(x):
		file = "./../game_stories/monsterfile.txt"
		lis = []
		listoflists = []
		i = 0
		new_line = ""
		with open(file, 'r') as infile:
			for line in infile:
				#print(line)
				if(line == " "):
					continue
				lis = line.split()
				#print(lis)
				if(lis[0] != None and lis[0] == str(x)):
					new_line = line[2:]

		return(new_line)
	print("This is get monster function coming up --->")
	#print(get_monster(x))		
	#print("End of get_monster")
	monster1 = Monster("Ulrich", 100, 200, "large")
	monster1.name, monster1.size = get_monster(x).split(" ")
	print(monster1.name)
	print(monster1.size)
	'''print(monster1.hp)
	print(monster1.max_hp)
	monster1.size = ("ExtraBig")
	print(monster1.size)
	hit = 2
	if(hit > 0):
		hp = monster1.hp - 1
		monster1.hp = (hp)
	print(monster1.hp)
	monster_list = []
'''	#monster = Monster("a", 1, 1, "a")
'''	for x in range(2):
		monster = Monster("a", 1, 1, "a")
		print("Your monster information")
		monster.name, monster.hp, monster.max_hp, monster.size =  input().split(" ")
		monster_list.append(monster)
		#print(monster_list[0].name)
		#print(monster_list[0].size)
	monster_list.append(monster1)	
	print(monster_list[0].name)
	print(monster_list[1].size)
	print(monster_list[2].name)

'''
