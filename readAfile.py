
x = "2"
file = "game_stories/monsterfile.txt"
def get_monster(file, x):
	lis = []
	listoflists = []
	i = 0
	with open(file, 'r') as infile:
		for  line in infile:
			if(line == " "):
				continue
			lis = line.split()
			#print(lis)
			if (lis[0] != None and  lis[0] == x):
				listoflists.append(lis)
			#print(listoflists)
			#listsoflists.apppend(lis[i])
			#i += 1
			#if(lis[0] == x):
			#	print(line)
	print(listoflists)

	for x in listoflists:
		print(x)

get_monster(file, x)
