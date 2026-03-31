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
