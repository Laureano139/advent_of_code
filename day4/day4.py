
# Input é uma matriz de n linhas e m colunas

def validBoundRange(x, y, sizeX, sizeY):
        return 0 <= x < sizeX and 0 <= y < sizeY

def challenge1():

    def search_word(grid, word):
        n, m = len(grid), len(grid[0])
        wordLength = len(word)
        counter = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i in range(n):
            for j in range(m):
                
                if grid[i][j] != word[0]:
                    continue

                for dirX, dirY in directions:
                    x, y = i, j
                    found = True

                    for k in range(wordLength):
                        if not validBoundRange(x, y, n, m) or grid[x][y] != word[k]:
                            found = False
                            break
                        x += dirX
                        y += dirY

                    if found:
                        counter += 1

        return counter

    word = "XMAS"
    with open("input.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    res = search_word(grid, word)
    print(f"Ocurrências de '{word}': {res}\n")
    
challenge1()



def challenge2():

    def searchMASCross(matrix):
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if matrix[i][j] == 'A':
                    d1_forward = matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S'
                    d1_backward = matrix[i - 1][j - 1] == 'S' and matrix[i + 1][j + 1] == 'M'

                    d2_forward = matrix[i - 1][j + 1] == 'M' and matrix[i + 1][j - 1] == 'S'
                    d2_backward = matrix[i - 1][j + 1] == 'S' and matrix[i + 1][j - 1] == 'M'

                    if (d1_forward or d1_backward) and (d2_forward or d2_backward):
                        count += 1
        return count

    with open("input2.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    r = searchMASCross(grid)
    print(f"Número de X-MAS encontrados : {r}\n")
    
challenge2()