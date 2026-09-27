type DimensionDict = dict[int, List[str]]

class Solution:
    def assignSubBox(self, coordinates: List[int]) -> int: 
        x = coordinates[0]
        y = coordinates[1]

        if x <= 2 and y <= 2:
            return 0
        if (x > 2 and x <= 5) and y <= 2:
            return 1
        if (x > 5 and x <= 8) and y <= 2:
            return 2
        if x <= 2 and (y > 2 and y <= 5):
            return 3
        if (x > 2 and x <= 5) and (y > 2 and y <= 5):
            return 4
        if (x > 5 and x <= 8) and (y > 2 and y <= 5):
            return 5
        if x <= 2 and (y > 5 and x <= 8):
            return 6
        if (x > 2 and x <= 5) and (y > 5 and y <= 8):
            return 7
        if (x > 5 and x <= 8) and (y > 5 and y <= 8):
            return 8
        else:
            return -1


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        indices = [0,1,2,3,4,5,6,7,8]
        row: DimensionDict = {key: [] for key in indices}
        col: DimensionDict = {key: [] for key in indices}
        subBox: DimensionDict = {key: [] for key in indices}

        for boardRowIndex in range(len(board)):
            for boardItemIndex in range(len(board)):
                boardItem = board[boardRowIndex][boardItemIndex]
                boardItemSubBox = self.assignSubBox([boardRowIndex, boardItemIndex])

                if boardItem in row[boardRowIndex] or boardItem in col[boardItemIndex] or boardItem in subBox[boardItemSubBox]:
                    return False

                if boardItem != ".":
                    row[boardRowIndex].append(boardItem)
                    col[boardItemIndex].append(boardItem)
                    subBox[boardItemSubBox].append(boardItem)        

        return True