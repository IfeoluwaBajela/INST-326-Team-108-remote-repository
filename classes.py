from argparse import ArgumentParser
import re 
import sys
import random
import time

class player():
    """Class for a player. Each player has some sort of name and a highscore 
    that is updated. 
    
    """
    def __init__(self, name, highscore = 0):
        self.name = name
        self.highscore = highscore
    
    def record_input(self):
        """Records the response for the player.
	
		Returns: 
	    resp (str): The player's response. 
	
    """
        resp = input(f"{self.name}, input your guess.")
        return resp
    
    
    def __repr__(self):
        return f"player(name={self.name}, highscore={self.highscore})"
    
    def __add__(self, other):
        """Creates a new player by adding the highscores of two players"""
        return player(self.name, self.highscore + other.highscore)
    
    def __eq__(self, other):
        """Compares two players highscores."""
        if not isinstance(other, player):
            return NotImplemented
        return self.highscore == other.highscore
    
    def __lt__(self, other):
        """Checks whether a player's highscore is less than another player's."""
        if not isinstance(other, player):
            return NotImplemented
        return self.highscore < other.highscore
    
    def __gt__(self, other):
        """Checks whether a player's highscore is greater than another 
            player's
            """
        if not isinstance(other, player):
            return NotImplemented
        return self.highscore > other.highscore

class game():
            
    def __init__(self, player):
        self.player = player
        self.points = 0
        self.categories = [
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
    def play(self):
        """Runs the full game loop."""
        used_categories = []

        print(f"Welcome, {self.player.name}!")

        while True:

            curr_cat = self.select_categories(used_categories)
            if curr_cat is None:
                print("No more categories! Game over.")
                break

            category_data = next(c for c in self.categories if c["name"] == curr_cat)
            questions = category_data["items"]
            print(f"\nCategory: {curr_cat}")

            player_guesses = []
            correct_answers = [q["answer"] for q in questions]

            for q in questions:
                print(f"\n{q['question']}")
                attempts = 3
                answered = False

                while attempts > 0:
                    guess = input("Your guess: ").strip()
                    self.guess_display(q['answer'], guess)
                    if guess.lower() == q["answer"].lower():
                        attempts_used = 3 - attempts + 1
                        self.points += self.calculate_points(attempts_used)
                        print(f"Correct! Points: {self.points}")
                        player_guesses.append(guess)
                        answered = True
                        break
                    else:
                        attempts -= 1
                        print(f"Wrong. Attempts left: {attempts}")

                if not answered:
                    print(f"The answer was: {q['answer']}")
                    player_guesses.append("")

            #self.display_score()
            
    def state (self, is_correct, current_round,  attempts, points):
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
            attempts_used = 3 - attempts
            points += self.calculate_points(attempts_used)
            current_round +=1
            attempts = 3
            print(f"Correct! New Round \nRound: {current_round}, Attempts: {attempts}, Points: {points}")
        return current_round, attempts, points    
        
    def guess_display(self, word, guess):
        """Displays the word and whether your guesses are correct or not. 

    args:
            word (string): The word that is being guesssed.
            guess (string): The guess that the player inputed

        side effects:
            Prints the player's guess and then prints 
            another line giving the results of the guess. 

    """
    
        word = word.upper()
        guess = guess.upper()
        extras = 0
        exes = ""
        
        if len(guess) > len(word):
            extras = len(guess) - len(word)
            exes = "X" * extras

        #if len(word) != len(guess):
         #   print("Error: Guess must be the same length as word!")
          #  return
        
        length_check = min(len(word), len(guess))
        
        results = ["B"] * len(word)
        word_list = list(word)

        for i in range(length_check):
            if guess[i] == word[i]:
                results[i] = "G"
                word_list[i] = None

        for i in range(length_check):
            if results[i] == "G":
                continue

            if guess[i] in word_list:
                    results[i] = "Y"
                    word_list[word_list.index(guess[i])] = None
        
        print("".join(results) + exes)
    
    def calculate_points(self, attempts_used):
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
            
    def record_score (self, category, player_guesses, correct_answer, score_history):
        ''' 
        Author:Aya Shrestha
        Calculates and stores the score the player recieved for that round.
        Parameters:
            category (str): the category chosen for that round 
            player_guesses (list): list of 5 strings (the player's guesses)
            correct_answers (str): list of 5 strings (the correct answers)
            score_history (list): A list of previous scores recorded
		Side Effects: Appends the new score_record dict to score_history.

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
        
    def display_score(self, score_record):
        '''
        Author:Aya Shrestha
		Technique: f-string containing expressions
        Displays the player's results of one round.

        Parameters:
            score_record(dict): The score record returned by record_round_score.
		Side Effects:
			Prints out round summary and encouraging messages based on the number of questions correct.
		Returns:
			None
        '''
        print("Total Score")
        print(f"Category: {score_record['category']}")
        print(f"Accuracy: {score_record['num_correct']}/5" ({score_record['num_correct']* 20}%)")
        print(f"Score: {score_record['score_percent']}%")

        if score_record['num_correct'] == 5:
            print("\nPerfect score! You really know your stuff")
        elif score_record['num_correct'] >= 3:
            print("\nNot bad! Keep it up :D")
        else: 
            print("\nKeep trying! You'll get the hang of it")

    def guess_select(self, answer, guess):
        """
        Author- Yahir Cruz
        Determines each letter's position status for one guess against the correct
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
    
    def run_question_timer(self, questions, time_limit=120):
        '''
        Author: Aya Shrestha
        Technique: Sequence Unpacking
        Runs through all 5 questiosn with a timer for each.

        Parameters:
            questions (list): List of question dictionaries.
            time_limit (int): Time allowed per question (120 seconds).
			
		Side Effects: Prints each question, a message when time is up, and a round summary.

        Returns:
            list: A list of the player's answers in order. An empty string is recorded if time is up and user has not answered.
        '''
        player_answers=[]

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

                player_answer = input("your guess: ").strip()

                if player_answer:
                    break
            player_answers.append(player_answer)

        results = [
            f" Q{i + 1}: {'Correct' if player_answers[i].lower() == questions[i]['answer'].lower()
            else 'Incorrect'} - answer was {questions[i]['answer']}"

            for i in range(len(questions))
        ]

        print("\n Round Summary")
        for result in results:
            print(result)

        return player_answers
            
            
    def select_categories(self,used_categories):
        """Author:Ifeoluwa Bajela
        Select a single unused category from options available
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
        
        for category in self.categories: 
            if category["name"] not in used_categories:
                available_categories.append(category)
                
        if not available_categories:    
            return None 
    
        selected_category = available_categories[0]    
        
        selected_category["items"].append(selected_category["items"].pop(0))
        
        used_categories.append(selected_category["name"])
        
        return selected_category["name"]
        
    def valid_category(self, category):
        """Author: Ifeoluwa Bajela 
        Regular expression meant to check and validate categories"""
       
        pattern = r"^[A-Za-z]+$"
        return bool(re.fullmatch(pattern,category))
       


    def play_again(self):
        """Ask whether the player wants to play the game again..  

            side effects:
                Ask for player input on whether the game returns. . 

            Returns:
                boolean: True or false depending on whether the player wants 
                to play again or not. 

        """
        while True: 
            resp = input("Would you like to play again (Y/N): ").strip().upper()

            if resp == "Y":
                return True
            elif resp == "N": 
                return False
            else:
                print ("Invalid input")        
        
    
def main(name):
    """ Creates the game and allows players to play it. 
    """
    gamer = player(name)
    g = game(gamer)
    
    con = True
    
    while con:
     
     g.play()
     con = g.play_again()    
         
    
def parse_args(arglist):
    """Parses argument command lines
    
        Expects two mandatory arguments:
        words - A list of words to be used for the game.
        players - names of a players. 
        
        Has an addational augment: 
        -r, --rules: If specfied showcases the rules before the player starts 
        playing.
        
        Args:
            arglist (list of strings): arguments from the command line
            
        Returns:
            namespace: The parsed arguments as a namespace. 
        
    """
     
    parser = ArgumentParser() 
    parser.add_argument("players", nargs = "*", help = "Player names")
    parser.add_argument("-r", "--rules", action= "store_true", help= "Displays"
                        "rules")
    
    return parser.parse_args(arglist)

def rules_display():
    """Displays rules of the game. To be called using -r or -rules. 
    Side Effects:
        Prints the rules of the games. 
    
    """
    
    print("--Rules-- \n Guess the name based on the question given."
          "You have two minutes to guess each name with each round having 5"
          "questions. The amount of rounds is dependent on user input. "
          "Depending on how well you answer you will be rewarded a set amount "
          "of points with first try being 30, 2nd 20, three tries 10 and none "
          "if failed. Good Luck! \n _________________________")

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.rules:
        rules_display()
    main(args.players)

# class WordSelection:

