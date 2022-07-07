class Node:
    def __init__(self):         # Instead of storing a boolean, we store the str which ends at that node.
                                # Children stores all the places where character is present. 
        self.str = None
        self.children = [ None]*26
    

class Trie:
    def __init__(self):     
        self.root = Node()
    
    
    def insert(self,word):

        curr = self.root
        for i in range(len(word)):          # We travel on the string and see whether or not the character is present, if not we insert it else we move on
            ch = word[i]

            if curr.children[ord(ch) - ord('a')] == None:
                curr.children[ord(ch) - ord('a')] = Node()

            curr = curr.children[ord(ch) - ord('a')]
        
        curr.str = word # At the end with store the str as a flag at the end.

    def search(self,word):  # Again, we travel char by char, if it is present we keep on moving, at any point if char doesnt match then the word isnt present.
        curr = self.root
        for i in range(len(word)):
            ch = word[i]

            if curr.children[ord(ch) - ord('a')] == None:
                return False
            curr = curr.children[ord(ch) - ord('a')]
        
        return curr.str == word # The prefix might be present but we check if the word ends there or not, we use the flag for it.

def findWords(board, words):
    def dfs(i,j,root):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return
            
        if root.children[ord(board[i][j]) - ord('a')] == None:      


            return
                                                            # The basic algorithm is to put all the words that we have to search in the grid
                                                            # in a Trie, now we travel over the crossword and try to make a word starting from that char
                                                            # Basically, giving a chance to all the characters to be a start, if it is present, we move 
                                                            # on to its adjacent elements.
                                                            # If the prefix is present we use the flag to see if the word is present or not.
        child = root.children[ord(board[i][j]) - ord('a')]
        if child.str != None:
            ans.add(child.str)
        visited[i][j] = True
        dfs(i,j+1,child)
        dfs(i+1,j,child)
        dfs(i-1,j,child)
        dfs(i,j-1,child)
        visited[i][j] = False
            
            
            
    trie = Trie()
    for word in words:
        trie.insert(word)
    ans = set()
    visited = [[False for i in range(len(board[0]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i,j,trie.root)
    return ans