

class Character():
	#This class is designed to make a character object
	def __init__(self, name, hp, max_hp):
		self._name = name
		self._hp = hp
		self._max_hp = max_hp

	@property
	def name(self):
	#getter function in decorator for name
		return self._name

	@name.setter
	#setter function in decorator for name
	def name(self, name):
		self._name = name


	@property
	#getter function in decorator hp
	def hp(self):
		return self._hp


	@hp.setter
	#setter function in decorator hp
	def hp(self, hp):
		self._hp = hp

	@property
	#getter function in decorator for max_hp
	def max_hp(self):
		return self._max_hp


	@max_hp.setter
	#setter function in decorator for max_hp
	def max_hp(self, max_hp):
		self._max_hp = max_hp

	
	def show_info(self):
		#show the hp, maxhp and name information for object
		print("Name: {0} HP: {1}  MAX_HP: {2}".format(self._name, self._hp, self._max_hp))
			
	def hp_hit(self):
		#decrement the hp
		if(self._hp != 0):
			self._hp -= 1
		print("HP hit function")
		return self._hp

if __name__ == "__main__":
	character1 = Character("Ulrich", 100, 200)
	print(character1.name)
	print(character1.hp)
	character1.hp = 3000
	print(character1.hp)
	character1.hp_hit()
	character1.show_info()
		

