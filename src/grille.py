class Grid:
    
    def __init__(self, puzzle = 81*'.'):
                        
        self.puzzle = puzzle
        if self.puzzle.count(".") > 0:
            self.full = False
        else:
            self.full = True
        
    def loadFromFile(num):
        """
            Charger un puzzle dans le fichier grids.sud
            Argument :
                - num : numéro du puzzle à charger
            Tests :
            >>> Grid.loadFromFile(0).puzzle[:10]
            '4.....8.5.'
        """
        pass
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        