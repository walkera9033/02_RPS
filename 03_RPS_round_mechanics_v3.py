# Main routine more efficient than v2


def check_rounds():
		while True: 
			response = input ("How many rounds: ")

			round_error = "please type either <enter> or an " \ "integer that is more than 0/n"


		  # If infinite mode not chosen, check response
			# is an integer that is more than 0
			if response != "":
				try:
					response = int(response)

					# If  response is too low, go back to
					# start of Loop 
					if response < 1:
						

