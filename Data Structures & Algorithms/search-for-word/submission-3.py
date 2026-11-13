class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # track seen items
        seen = set()
        # helper function takes y, x, word_i
        def helper(y, x, word_i):
            # base case: if we're out of bounds of board, we're not the right letter, or we've been seen before, exit
            if y >= len(board) or y < 0 or x >= len(board[y]) or x < 0 or board[y][x] != word[word_i] or (y,x) in seen:
                return False
            # if we're at the end of the word and we equal the last letter, return true

            if word_i + 1 == len(word):
                return True
            # add curr y/x to seen
            seen.add((y,x))
            # recurse down every direction and increase 
            if helper(y-1, x, word_i+1):
                return True
            if helper(y+1, x, word_i+1):
                return True
            if helper(y, x-1, word_i+1):
                return True
            if helper(y, x+1, word_i+1):
                return True

            seen.remove((y,x))
            return False


        # for loop goes over every letter in the board
        for y in range(len(board)):
            for x in range(len(board[y])):
                # if helper return True return True
                if helper(y,x,0):
                    return True
                seen = set()


        return False