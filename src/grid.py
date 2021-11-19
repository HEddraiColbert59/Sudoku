from case import Case
class Grid:
    
    def __init__(self, puzzle = 81*'.'):
                        
        self.puzzle = puzzle
        self.initCases()
        self.puzzleNow = self.casesToString()
        
        if self.puzzle.count(".") > 0:
            self.full = False
        else:
            self.full = True
            
        
    def loadFromFile(num):

        file = open("data/grids.sud", 'r')
        lines = file.readlines()
        return Grid(lines[num][:-1])
    
    def initCases(self):
        
        self.cases = []
        
        for i in range(81):
            if self.puzzle[i] == ".":
                self.cases.append(Case(i))
            else:
                self.cases.append(Case(i, int(self.puzzle[i])))

    
        
                
    def casesToString(self):
        """
            Retourne une chaine de caractère représentant le Sudoku
            Permet de faire la comparaison entre l'état initial du puzzle
            et l'état après ajout de valeurs
            
            Cette méthode est appelée lors de l'instanciation de l'objet. Elle crée alors
            un attribut puzzleNow. Elle est également appelée lors d'un changement d'une
            valeur de case.
        
            Tests :
            >>> S = Grid()
            >>> S.puzzleNow == 81*'.'
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.cases[0].value = 5
            >>> S.casesToString()[0] == '5'
            True
        """
        S = ""
        for i in range(81):
            if self.cases[i].value == None:
                S += "."
            else:
                S += f"(self.cases[i].value)"       
        return S

    def setValue(self, position, value):
        """
            Méthode permettant de modifier la valeur d'une case à une position donnée.
            Cette méthode doit mettre à jour l'attribut puzzleNow.
            Attention, on ne doit pas pouvoir modifier une valeur qui a été placée initialement.
            
            Tests :
            >>> S = Grid()
            >>> S.setValue(0, 8)
            >>> S.puzzleNow[0] == '8'
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.setValue(0, 7)
            >>> S.puzzleNow[0] == '7'
            False
        """


    def __repr__(self):
        """
            Méthode de représentation d'un Sudoku
        """
        S = ''
        for i in range(81):
            if (i+1)%9==0:
                S += f'|{self.puzzleNow[i]}|\n'
            else:
                S += f'|{self.puzzleNow[i]}'
        return S   
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

