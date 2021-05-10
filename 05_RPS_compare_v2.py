# RPS Component 3 - Compare user choices and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
	user_index = 0
	for item in rps_list:
		user_choice = rps_list[user_index]
		comp_choice = rps_list[comp_index]
		user_index += 1


		result = ""

		# Compare options between computer and user

		# if the choices are the same, it's a tie
		if comp_choice == user_choice:
			result = "tie"

		# three ways to win...
		elif comp_choice == "rock" and user_choice == "paper":
			result = "win"
		elif comp_choice == "scissors" and user_choice == "rock":
			result = "win"
		elif comp_choice == "paper" and user_choice == "scissors":
			result = "win"

		# if you don't tie / win, you lose
		else:
			result = "lose"

		print("User: {} vs Computer: {} - {}".format(user_choice, comp_choice, result))

		comp_index += 1