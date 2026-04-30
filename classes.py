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
    
