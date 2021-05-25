def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
 
        if response == "yes" or response == "y":
            response = "yes"
            return response
 
        elif response == "no" or response == "n":
            response = "no"
            return response
def instructions():
	print ("**** How to Play ****") 
	print()
	print ("In this particular game, your aim to win your chosen amount of rounds of Rock, Paper, Scissors against a computer genarator. Each round you will have to chose either r / p / s ")
	print () 
	print("*** Game Rules***")
	print()
	print("Rock beats scissors")
	print("Scissors beats paper")
	print("Paper beats rock")
	print()
	print("GOOD LUCK!!!🤞")	
	return "" 
 if played_before = yes_no("Have you played the game before? ")
 
if played_before == "no":
    instructions()
 
print("program Continues")