
def day2():
    with open('input.txt') as f:
        lines = f.readlines()

        cleanedLines = [line.strip() for line in lines if line.strip()] # Usei o strip para remover o \n
        arrays = [list(map(int, line.split())) for line in cleanedLines]
    
    valid = 0

    for arr in arrays:
        foundValid = False
        for index in range(len(arr) - 1):
            diff = abs(arr[index] - arr[index + 1])
            if 1 <= diff <= 3 and arr[index] > arr[index + 1]:
                valid += 1
                foundValid = True
            elif 1 <= diff <= 3 and arr[index] < arr[index + 1]:
                valid += 1
                foundValid = True
            else:
                valid += 0
        if foundValid:
            print(arr)
    print(valid)

day2()