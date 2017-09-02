

class Character():
	def __init__(self, name, hp, max_hp):
		self._name = name
		self._hp = hp
		self._max_hp = max_hp

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name


	@property
	def hp(self):
		return self._hp


	@hp.setter
	def hp(self, hp):
		self._hp = hp

	@property
	def max_hp(self):
		return self._max_hp


	@max_hp.setter
	def max_hp(self, max_hp):
		self._max_hp = max_hp

	
	def show_info(self):
		print("Name: {0} HP: {1}  MAX_HP: {2}".format(self._name, self._hp, self._max_hp))
			
	def hp_hit(self):
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
		

