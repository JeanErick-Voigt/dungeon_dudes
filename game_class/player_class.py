from game_class.character_class import Character


class Player(Character):
	def __init__(self, name, hp, max_hp):
		super().__init__(name, hp, max_hp)
		self._loot = {}
	
	
	@property
	def loot(self):
		if not self._loot:
			print("empty bag")

		else:
			for key in self._loot:
				print("contents of loot: %s" %key, sep="\n")

	@loot.setter
	def loot(self, item):
		if not self._loot:
			self._loot[item] = 1
			return
		
		elif item not in  self._loot:
			self._loot[item] = 1	
		
		else:
			for key in self._loot:
				if  self._loot[item]:
					self._loot[item] += 1
		return self._loot

	def use_item(self, item):
		if item not in self._loot:
			print("You do not have any %s" %item)
		else:
			self._loot[item] -= 1

		return(self._loot[item]) 

	def show_contents(self):
		print("Contents of bag")
		for key in self._loot:
			print("Item: {0}, Amount: {1}".format(key, self._loot.get(key)))


if __name__ == "__main__":
	hero = Player("Johnny", 100, 200)
	print(hero.name)
	hero.loot = "gold"
	hero.loot
	hero.loot = "gold"
	hero.loot = "silver"
	hero.loot = "sneak attack"
	hero.loot = "gold"
	hero.loot
	hero.show_contents()

	hero.use_item("gold")
	print("Contents")
	hero.show_contents() 		
