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


# get computer choice
	comp_choice = random.choice(rps_list[:-1])
	print("Comp Choice: ", comp_choice)

	chose = choice_checker("chose rock / paper / scissors (r/p/s): ", rps_list, "Please chose from rock, Paper / scissors (or xxx to quit).")

  # End game if exit code is typed
      if choose == "xxx":
			  break

    # End game if round entered is finished
 
    # Compare options/choices between computer choice and User choice 
    # if Choices are the same, it is a tie.
 
    if comp_choice == choose:
        result = "tie"
        # three ways to win...
    elif comp_choice == "rock" and choose == "paper":
        result = "win"
    elif comp_choice == "scissors" and choose == "rock":
        result = "win"
    elif comp_choice == "paper" and choose == "scissors":
        result = "win"
 
    # if you don't tie / win, you lose
    else:
        result = "lose"
        
    print("User: {} vs Computer: {} - {}".format(choose, comp_choice, result))
    print()



 
    if rounds!= "" and rounds_played >= rounds - 1:
        break
 
    # *** rest of loop / game ***
    print("You chose {}". format (choose))
 
    rounds_played += 1
 
# Ask user if they want to see their game history.
# if 'yes' show game history
 
# Show statistics
 
# end game
print()
print("Thanks for playing")
print()
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