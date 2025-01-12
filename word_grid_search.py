"""
Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Examples:
Input:
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Input:
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
Output: []
"""


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    trie = {}
    result = []
    rows, cols = len(board), len(board[0])

    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = word  # end of word marker

    def dfs(row, col, parent):
        if (char := board[row][col]) not in parent:
            return

        node = parent[char]  # get the next trie node

        if "#" in node:
            result.append(node["#"])
            del node["#"]

        board[row][col] = None  # mark as visited

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = row + dx, col + dy
            if 0 <= x < rows and 0 <= y < cols and board[x][y] is not None:
                dfs(x, y, node)

        board[row][col] = char  # backtrack

        if not node:
            del parent[char]

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, trie)

    return result


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(find_words(board, words))

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print(find_words(board, words))
