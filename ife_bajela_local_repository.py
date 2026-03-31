""" Pratice adding and commiting to a local repository"""
class Repository:
    """A local repository to store my files and edit history
    
    Attributes:
        Name (str): Name of repository 
        Files(list): List of files in working directorygit
    """
    
    def __init__(self, name):
     """A innit function with two paramaters. 
     
     Attributes:
        Name (str): Name
        Files (list): A list of files
    """  
        self.name = name
        self.files = []
    
class Guess: 
    """
    A class used to represent a players guess
    This class is used for storing the guess word and the feeback depending 
    on the players guess.
    
    Attributes:
        word(str): The player's guess
        list(str): A list showing the correctness of the letter/word being
        used"""
    def __init__(self, word):
        