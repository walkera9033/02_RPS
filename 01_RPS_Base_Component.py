import random 
 

# Functions go here

def check_rounds():
		while True:
			response = input("How many rounds: ")

			round_error = "Please type either <enter" / "or an integer that is more than 0\n"	

			if response != "":
				try:
					response = int(response)

					if response < 1:
						print(round_error)
					continue
				except ValueError:
					print(round_error)
				continue
		
		
				return response 

# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
choose_instructions = "Please choose rock (r), paper" / "(p) or scissors (s)"	



# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

  # Start of Game Play Loop

  # Rounds Heading
	print()
	if rounds =="":
		 heading = "continuous Mode :" \
		"Round {}".format(rounds_played + 1)
	else:  
		heading = "Round {} of " \
		"{}".format(rounds_played + 1, rounds)

	print(heading)
	choose = input("{} or 'xxx' to " "end: ".format(choose_instructions))

		# End game if exit code is typed 
	if choose == "xxx":
		break




# Ask user if they want to see their game history.
# If 'yes' show game history