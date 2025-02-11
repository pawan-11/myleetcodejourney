class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def help(i, j, subword):
            if len(subword) == 0:
                return True
            if subword[0] != board[i][j]:
                return False
            visited[i][j] = True

            if i+1 < len(board) and not visited[i+1][j] and help(i+1, j, subword[1:]):
                return True
            if i-1 > -1 and not visited[i-1][j] and help(i-1, j, subword[1:]):
                return True
            if j-1 > -1 and not visited[i][j-1] and help(i, j-1, subword[1:]):
                return True
            if j+1 < len(board[0]) and not visited[i][j+1] and help(i, j+1, subword[1:]):
                return True
            visited[i][j] = False
            return len(subword) <= 1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if help(i,j,word):
                    return True
        return len(word) == 0
                    