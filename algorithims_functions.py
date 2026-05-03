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
    else: 
        print (f"Round: {round}, Attempts: {attempts}, Points: {self.points}")

		
def record_score (category, player_guesses, correct_answer, score_history):
	''' 
	Author:Aya Shrestha
	Calculates and stores the score the player recieved for that round.
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
		if player_guesses[i].lower() == correct_answer[i].lower():
			num_correct += 1
	score_percent = (num_correct / 5) * 100
	score_record = {
		"category": category,
		"num_correct": num_correct,
		"score_percent": score_percent
		}

	score_history.append(score_record)
	return score_record	
def display_score(score_record):
	'''
	Author:Aya Shrestha
	Displays the player's results of one round.

	Parameters:
		score_record(dict): The score record returned by record_round_score.
	'''
	print("Total Score")
	print(f"Category: {score_record['category']}")
	print(f"Accuracy: {score_record['num_correct']}/5")
	print(f"Score: {score_record['score_percent']}%")

	if score_record['num_correct'] == 5:
		print("\nPerfect score! You really know your stuff")
	elif score_record['num_correct'] >= 3:
		print("\nNot bad! Keep it up :D")
	else: 
		print("\nKeep trying! You'll get the hang of it")

def display_score_history(score_history):
	'''
	Author: Aya Shrestha
	Technique: Comprehension
	Displays the score history to the player.

	Parameters:
		score_history(list): The list of score records
	'''
	print("\nScore History")
	records = [
    f"Round {i+1}: {score_history[i]['category']} | {score_history[i]['num_correct']}/5 correct | {score_history[i]['score_percent']}%"
    for i in range(len(score_history))
]
for record in records:
    print(record)

def guess_select(answer, guess):
	"""Determines each letter's position status for one guess against the correct
	word based on its position and presence
	Arguments:
		answer (Str): the actual targeted word the player is trying to guess
		guess (str): The players 5 lettered guess provided by the player
	Side effects:
		converts the answer and guess strings into lowercase for case sensitivity
		"""
	answer = answer.lower()
	guess = guess.lower()
	result = []
	answer_list = list(answer)

	statuses = ["absent", "absent", "absent", "absent"]

	for i in range(5):
		if guess[i] == answer_list[i]:
			statuses[i] = "correct"
			continue
		
		letter = guess[i]
		if letter in answer_list:
			statuses[i] = "present"
			answer_list.remove(letter)
	
	for i in range(5):
		item = {
			"letter": guess[i],
			"status": statuses[i]
		}
		results.append(item)
	return results
def run_question_timer(questions, time_limit=120):
	'''
	Author: Aya Shrestha
	Technique: Sequence Unpacking
	Runs through all 5 questiosn with a timer for each.

	Parameters:
		questions (list): List of question dictionaries.
		time_limit (int): Time allowed per question (120 seconds).

	Returns:
		list: A list of the player's answers in order.
	'''
	players_answers[]

	for question_dict in questions:
		question, answer = (
			question_dict["question"]
			question_dict["answer"]
		)
		print(f"{question})

		start_time = time.time()
		player_answer = ""

		while True:
			elapsed = time.time() - start_time

			if elapsed >= time_limit:
				print(" Time's up!")
				break

			player_answer = get_player_guess(answer)

			if player_answer:
				break
		player_answers.append(player_answer)

	results = [
		f" Q{i + 1}: {"Correct" if player_answers[i].lower() == questions[i]['answer'].lower() 
		else "Incorrect"} - answer was {questions[i]["answer"]}"

		for i in range(len(questions))
	]

	print("\n Round Summary")
	for result in results:
		print(result)

	return player_answers
		
		

def select_categories(categories, used_categories):
    """Select a single unused category from options available
    Arguments: 
    
    categories(list of dict): A list where each element is a dictionary 
    representing each category to be used.
    
    Used categories(str): All the categories that have been 
    used in a previous round that should be avoided. 
    
    Returns:
    str: The name of the selected category for the current round.
    Returns None if no unused categories are available.

    Side Effects:
    Updates the used_categories list by adding the selected category
    name to prevent reuse in future rounds.

    """
    
    
    available_categories = []
    
    for category in categories: 
        if category["name"] not in used_categories:
            available_categories.append(category)
            
    if not available_categories:    
        return None 
   
    selected_category = available_categories[0]    
    
    options = selected_category["options"]
    selected_option = options[0]
    
    selected_category["options"].append(selected_category["options"].pop(0))
    
    used_categories.append(selected_category["name"])
    
    return selected_category["name"] 
	
	categories = [{"name": "Buildings","options":["ESJ","STAMP","Mckelding"]},
              {"name":"Majors","options":["Information Science","Mathematics",
                "Biology"]}, {"name":"Colleges","options":["CMNS","BSOS","SPH"]}
              ]
