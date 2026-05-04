from argparse import ArgumentParser
import re 
import sys

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




class game():
    
    def __init__(self, word):
        pass
    
def main():
    """ Creates the game.
    """
    pass
    
def parse_args(arglist):
    """Parses argument command lines
    
        Expects two mandatory arguments:
        words - A list of words to be used for the game.
        players - names of a players. 
        
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
    
    print("--Rules-- \n "
          "Guess the name based off the question given! \n"
          "You have two minutes to guess each name with each round having 5"
          "questions. The amount of rounds is dependent on user input. \n"
          "Depending on how well you answer you will be rewarded a set amount"
          " of points. \n 1st try 30 points \n 2nd try 20 points. \n"
          "3rd try 10 points \n and none if failed. Good luck \n"
          "_______________________")
    
if __name__ == "main":
    args = parse_args(sys.argv[1:])
    if args.rules:
        rules_display()
    main()
