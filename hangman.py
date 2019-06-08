cg = "" #correct guesses
wg = "" #wrong guesses
turns = 5
word = "secret"
f = 0

def current_guessed():
	global cg, word, f
	f = 0
	for char in word:
		if char in cg:
			print(char, end="")
		else:
			print("_", end="")
			f = -1
	if(f==0):
		print("\nYou Won")
		exit()
		

def check(g):
	global cg, wg, turns, word
	if g in word:
		cg += g
	else:
		wg += g
		turns -= 1

while(turns>0):
	print("You have " + str(turns) + "turns left.")
	g = input("Enter your guess: ")
	check(g)
	current_guessed()

if(turns<=0 and f!=0):
	print("You Loose. Better luck next time")
