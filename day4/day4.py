
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

    def searchMASCross(grid):
        n, m = len(grid), len(grid[0])
        count = 0
        word = "MAS"

        for i in range(n):
            for j in range(m):
                for dirX1, dirY1 in [(1, 1), (-1, -1)]:
                    for dirX2, dirY2 in [(1, -1), (-1, 1)]:
                        x1, y1 = i, j
                        found1 = True
                        for k in range(len(word)):
                            if not validBoundRange(x1, y1, n, m) or grid[x1][y1] != word[k]:
                                found1 = False
                                break
                            x1 += dirX1
                            y1 += dirY1

                        x2, y2 = i, j
                        found2 = True
                        for k in range(len(word)):
                            if not validBoundRange(x2, y2, n, m) or grid[x2][y2] != word[k]:
                                found2 = False
                                break
                            x2 += dirX2
                            y2 += dirY2

                        if found1 and found2:
                            count += 1
        return count

    with open("input2.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    r = searchMASCross(grid)
    print(f"Número de X-MAS encontrados : {r}\n")
    
challenge2()