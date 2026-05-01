from argparse import ArgumentParser
import re 
import se 

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
    
def parse_args(arglist):
    """Parses argument command lines
    
        Expects two mandatory arguments:
        words - A list of words to be used for the game.
        players - names of a players. 
        
        Args:
            arglist (list of strings): arguments from the command line
            
        Returns:
        
    """
    #Will add more arguments depending on if we need them or not.
    
    parser = ArgumentParser() 
    parser.add_argument("words", help = "path to word list from a text file.")
    parser.add_argument("players", nargs = "*", help = "Player names")
    
    return parser.parse_args(arglist)