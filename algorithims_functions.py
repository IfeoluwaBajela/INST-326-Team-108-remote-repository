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
    
