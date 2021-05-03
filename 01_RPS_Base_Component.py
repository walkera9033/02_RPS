import random 

 
# Functions go here
def check_rounds():
	while True:
		response = input("How many rounds: ")

		round_error = "Please type either <enter / or an integer that is more than 0\n"	


		# if infinite mode not chosen, check response
		# is an integer that is more than 0
		if response != "":
			try:
				response = int(response)

				# if response is too low, go back to
				# start of loop
				if response < 1:
					print(round_error)
					continue

				else:
					return response

			# if response is not an integer, go back to
			# start of loop
			except ValueError:
				print(round_error)
				continue

		else:
			return response
			


def choice_checker (question, valid_list, error):
	valid = False
	while not valid :

		# Ask user for choice
		response = input(question).lower()

		for item in valid_list:
			if response == item[0]:
				return item
			elif response == item:
				return item

		print(error)
				

# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
choose_instructions = "Please choose rock (r), paper (p) or scissors (s)"	

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

	# Start of Game Play Loop

	# Rounds Heading for continuous mode / specific # of rounds
	print()
	if rounds == "":
		heading = "continuous Mode:  Round {}".format(rounds_played + 1)
	else:   
		heading = "Round {} of {}".format(rounds_played + 1, rounds)

	print(heading)
  
		
	# Ask user for choice and check its valid
	choose_error = "Please choose from rock  / paper / scissors (or xxx to quit)"
	choose = choice_checker(choose_instructions, rps_list, choose_error)
	
# get computer choice
	comp_choice = random.choice(rps_list[:-1])
	print("Comp Choice: ", comp_choice

# compare choices

	# End game if exit code is typed 
	if choose == "xxx":
	  	 break

	#  **** rest of loop / game *****	
	print ("You chose {}".format(choose))

	rounds_played += 1

	# end game if requsted # of rounds has been played
	if rounds_played == rounds:
		break


# Ask user if they want to see their game history.
# If 'yes' show game history