# RPS Component 3 - Compare user choices and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
	user_index = 0
	for item in rps_list:
		user_choice = rps_list[user_index]
		comp_choice = rps_list[comp_index]
		user_index += 1

		# Compare options
