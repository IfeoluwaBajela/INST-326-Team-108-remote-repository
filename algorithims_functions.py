def state (is_correct, current_round, answers, attempts, points):
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
    
    if not is_correct and attempts == 0:
        current_round += 1
        attempts = 3
        print (f"""Try again. New Round \n 
                Round: {current_round}, Attempts: {attempts}, Points: {points}""")
   
    elif not is_correct and attempts != 0:
        attempts -= 1
        print (f"""Try again \n 
                Round: {current_round}, Attempts: {attempts}, Points: {points}""")
    
    elif is_correct:
        attempts_used = 4 - attempts
        points += calcualte_points(attempts_used)
        current_round +=1
        attempts = 3
        print(f"Correct! New Round \nRound: {current_round}, Attempts: {attempts}, Points: {points}")
    return current_round, attempts, points

def record_input(player_name):
    """Records the response for the player.
	
		Returns: 
	    resp (str): The player's response. 
	
    """
    resp = input(f"{self.name}, input your guess.")
    return resp

def word_display(word, guess):
	"""Displays the word """
 
	#Might go into another method depending on how code looks
 
	word = word.upper()
	guess = guess.upper()
	
	if len(word) != len(guess):
		print("Error: Guess must be the same length as word!")
		return
	
	results = ["B"] * len(word)
	word_list = list(word)

	for i in range(len(word)):
		if guess[i] == word[i]:
			results[i] = "G"
			word_list[i] = None

		for i in range(len(word)):
			if results[i] == "G":
				continue

			if guess[i] in word_list:
				results[i] == "Y"
			word_list[word_list.index(guess[i])] = None
    
	print(guess)
	print("".join(results))
 
def calculate_points(attempts_used):
    """
    Calculates points based on how many attempts the player used.
    
    Arguments:
        attempts_used (int): The number of attempts the player used (1, 2, or 3)
            	 0 indicates the player failed to guess correctly.
    
    Returns:
        int: Total points earned for that question. (30, 20, 10, or 0)
    """
    points_map = {1: 30, 2: 20, 3: 10}
    return points_map.get(attempts_used, 0)
		
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
	results = []
	answer_list = list(answer)
	statuses = ["absent"]*5

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

import time

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
	players_answers=[]

	for question_dict in questions:
		question, answer = (
			question_dict["question"],
			question_dict["answer"]
		)
		print(f"\nQuestion: {question}")
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
		
		
categories = [
    {
        "name": "Majors",
        "items": [
            {"question": "This major focuses on how people interact with data, technology, and information systems.", "answer": "Information Science"},
            {"question": "This major studies living organisms.", "answer": "Biology"},
            {"question": "This major focuses on programming, algorithms, and software development.", "answer": "Computer Science"},
            {"question": "This major deals with circuits, power systems, and electronic devices.", "answer": "Electrical Engineering"},
            {"question": "This major focuses on analyzing, developing, and evaluating solutions to complex societal issues.", "answer": "Public Policy"}
        ]
    },
    {
        "name": "Buildings",
        "items": [
            {"question": "This building is the central hub for international education, cultural programs, and academic units.", "answer": "HJ Patterson"},
            {"question": "This facility is UMD's main gym and fitness center for students.", "answer": "Eppley Recreation Center"},
            {"question": "This is UMD's largest library, located at the heart of campus.", "answer": "McKeldin Library"},
            {"question": "This building is UMD's main student union, with activities, study spaces, and the campus bookstores.", "answer": "STAMP"},
            {"question": "This building is home to UMD's computer science program.", "answer": "Brendan Iribe Center"}
        ]
    },
    {
        "name": "Minors",
        "items": [
            {"question": "This minor teaches you how to analyze and interpret large sets of data.", "answer": "Data Science"},
            {"question": "This minor explores stars, planets, galaxies, and the universe.", "answer": "Astronomy"},
            {"question": "This minor focuses on developing skills in fiction, poetry, and storytelling.", "answer": "Creative Writing"},
            {"question": "This minor covers how businesses use data to make smarter decisions.", "answer": "Business Analytics"},
            {"question": "This minor covers property markets, investment, and land development.", "answer": "Real Estate"}
        ]
    },
    {
        "name": "Colleges",
        "items": [
            {"question": "This is the college code for the College of Computer, Mathematical, and Natural Sciences at UMD.", "answer": "CMNS"}, 
            {"question": "This is the college code for the College of Information Studies at UMD.", "answer": "INFO"},
            {"question": "This is the college code for the A. James Clark School of Engineering at UMD.", "answer": "ENGR"},
            {"question": "This is the college code for the College of Arts and Humanities at UMD.", "answer": "ARHU"},
            {"question": "This is the college code for the College of Business and Management at UMD.", "answer": "BMGT"}
        ]
    }
]

def select_categories(self):
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
    
    selected_category["items"].append(selected_category["items"].pop(0))
    
    used_categories.append(selected_category["name"])
    
    return selected_category["name"]

def valid_category(category):
    pattern =  r"^[A-Za-z ]+$"

    return bool(re.fullmatch(pattern, category))

def validate_guess_pro(guess, word_list):
	is_valid, message = validate_guess(guess)
	if not is_valid:
		return False, message

	if guess.lower() not in [w.lower() for w in available_categories:
			return False, "That is not a recognized word."

	return True, "Valid guess"
