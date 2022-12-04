class AiTickTackToe:
    def __init__(self):
        self.grid = self.initialiseGrid()
        self.occupied = {}
        
    def initialiseGrid(self):
        grid = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                grid[row][col] = 3*row + (col+1)
        return grid
    

    def validateMove(self, humanMove):
        if humanMove not in range(1, 10):
            return {"message": "Move out of range!!"}
        if humanMove in self.occupied:
            return {"message": "Already occupied.."}
        return True

    def bestAiMove(self, grid):
        score = float("inf")
        for cell in self.findEmptyCells(grid):
            row, col = cell
            current = grid[row][col]
            grid[row][col] = "O"
            currentScore = int(self.playMinMax(grid, False))
            grid[row][col] = current
            if currentScore < score:
                bestRow, bestCol = row, col
                score = currentScore
        return bestRow, bestCol
        
    def playGame(self):
        grid = self.grid
        while not self.checkIfFinished(grid):
            self.printGrid()
            move = int(input("Enter the cell where you wish to play move: "))
            ifValid = self.validateMove(move)
            if ifValid is not True:
                return ifValid["message"]
            row = move // 3 if move % 3 != 0 else move // 3 -1
            col = move % 3 -1 if move % 3 != 0 else 2
            grid[row][col] = "X"
            if self.checkIfFinished(grid):
                break
            nextRow, nextCol = self.bestAiMove(grid)
            grid[nextRow][nextCol] = "O"
        return "winner is: " + str(self.checkIfFinished(grid))


    def playMinMax(self, grid, isAiMove):
#         self.printGrid()
        result = self.checkIfFinished(grid)
        if result != False:
            return result
        emptyCells = self.findEmptyCells(grid)
        currentResult = float("inf") if isAiMove else float("-inf")
        if isAiMove:
            for cell in emptyCells:
                row, col = cell
                current = grid[row][col]
                grid[row][col] = "O"
                score = self.playMinMax(grid, not isAiMove)
                score = int(score)
                grid[row][col] = current
                if score < currentResult:
                    currentResult = score
                
#             grid[bestRow][bestCol] = "O"
        else:
            for cell in emptyCells:
                row, col = cell
                current = grid[row][col]
                grid[row][col] = "X"
                score = self.playMinMax(grid, not isAiMove)
                score = int(score)
                grid[row][col] = current
                if score > currentResult:
                    currentResult = score
                   
        return currentResult
    

    
    def findEmptyCells(self, grid):
        result = []
        for row in range(3):
            for col in range(3):
                if grid[row][col] not in ("X", "O"):
                    result.append((row, col))
        return result

        
        
        
    def printGrid(self):
        grid = self.grid
        print("------------")
        print("|", grid[0][0], "|", grid[0][1], "|", grid[0][2], "|")
        print("------------")
        print("|", grid[1][0], "|", grid[1][1], "|", grid[1][2], "|")
        print("------------")
        print("|", grid[2][0], "|", grid[2][1], "|", grid[2][2], "|")
        print("------------")

    def playGameHelper(self, grid):
        pass
    
    def checkIfFinished(self, grid):
        rowWinner = self.checkRows(grid)
        colWinner = self.checkCols(grid)
        digonalWinner = self.checkDigonals(grid)
        ifTie = self.checkIfTie(grid)
        winner = rowWinner or colWinner or digonalWinner
        if winner in ("X", "O"):
            return "1" if winner == "X" else "-1"
        return "0" if ifTie else False


    def checkIfTie(self, grid):
        for row in range(3):
            for col in range(3):
                if grid[row][col] in range(1, 10):
                    return False
        return True

    
    def checkRows(self, grid):
        if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2]:
            return grid[0][0]
        if grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2]:
            return grid[1][0]
        if grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2]:
            return grid[2][0]
        return False
    
    def checkCols(self, grid):
        if grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0]:
            return grid[0][0]
        if grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1]:
            return grid[0][1]
        if grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]:
            return grid[0][2]
        return False

    def checkDigonals(self, grid):
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            return grid[0][0]
        if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
            return grid[0][2]
        return False

    
    
game = AiTickTackToe()
game.initialiseGrid()
game.playGame()