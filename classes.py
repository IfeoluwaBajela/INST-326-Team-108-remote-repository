from argparse import ArgumentParser
import re 
import se 
import sys
import random

with open("keywords.txt", "r") as file:
    w_bank = [line.strip().lower() for line in file if line.strip()]

    major_word = random.choice(w_bank)
    
class player():
    """Class for a player. Each player has some sort of name and a highscore 
    that is updated. 
    
    """
    def __init__(self, name, highscore):
        self.name = name
        self.highscore = highscore
        pass
    
    def __repr__(self):
        return f"player(name={self.name}, highscore={self.highscore})"
    
    def __add__(self, other):
        """Creates a new player by adding the highscores of two players"""
        return player(self.name, self.highscore + other.highscore)
    
    def __eq__(self, other):
        """Compares two players highscores."""
        if not isinstance(other, player):
            return NotImplemented
        return self.highscore == self.highscore
    
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
    

    def __init__(self):
        pass
    
def main():
    """ Creates the game and allows players to play it. 
    """
    pass
    
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
    #Will add more arguments depending on if we need them or not.
     
    parser = ArgumentParser() 
    parser.add_argument("words", help = "path to word list from a text file.")
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
    main()

# class WordSelection:

