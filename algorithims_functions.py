def state (answers, round, attempts):
    """""
    Updates the rounds and attempts a player takes when guessing. After each 
    guess prints whether the player got it right or not, if the round has 
    updated and showcases current round, attempts and points. 
    
    Arguments: 
	    Answers (Dictionary): Dictonary of answers
	    Round(int): The current round.

    Side Effects:
	    Updates the round and prints a message telling the score, round and 
        events. Prints a statment into the command line. 
    """""
    
    if correct == False and attempts == 0:
        round += 1
        attempts == 3
        print (f"""Try again. New Round \n 
                Round: {round}, Attempts: {attempts}, Points: {self.points}""")
    elif correct == False and attempts != 0:
        attempts -= 1
        print (f"""Try again \n 
                Round: {round}, Attempts: {attempts}, Points: {self.points}""")
    elif correct == True: 
        round += 1
        attempts == 3
        print (f"""Correct!!! New Round \n 
                Round: {round}, Attempts: {attempts}, Points: {self.points}""")
		
def record_score (categories, player_guesses, correct_answer, score_history):
	''' Calculates and stores the score the player recieved for that round.
	Parameters:
		category (str): the category chosen for that round 
		player_guesses (list): list of 5 strings (the player's guesses)
		correct_answers (str): list of 5 strings (the correct answers)
		score_history (list): A list of previous scores recorded

	Returns:
		dict: records and stores the score for this round.
	'''

	num_correct = 0
	for i in range(5):
		if players_guess[i].lower() == correct_answer[i].lower():
			num_correct += 1
	score_percent = (num_correct / 5) * 100
	score_record = {
		"category": category
		"num_correct": num_category
		"score_percent": score_percent
		}

	score_history.append(score_record)
	return score_record	
		
	
