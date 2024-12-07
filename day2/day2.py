
def challenge1():
    with open('input.txt') as f:
        lines = f.readlines()

        cleanedLines = [line.strip() for line in lines if line.strip()] # Usei o strip para remover os \n
        arrays = [list(map(int, line.split())) for line in cleanedLines]
    
    valid = 0

    for arr in arrays:
        is_increasing = all(1 <= arr[i+1] - arr[i] <= 3 for i in range(len(arr) - 1))
        is_decreasing = all(1 <= arr[i] - arr[i+1] <= 3 for i in range(len(arr) - 1))
        
        if is_increasing or is_decreasing:
            valid += 1
    print(valid)

challenge1()

def challenge2():
    with open('input2.txt') as f:
        lines = f.readlines()

        cleanedLines = [line.strip() for line in lines if line.strip()]
        arrays = [list(map(int, line.split())) for line in cleanedLines]
    
    valid = 0

    for arr in arrays:
        is_increasing = all(1 <= arr[i+1] - arr[i] <= 3 for i in range(len(arr) - 1))
        is_decreasing = all(1 <= arr[i] - arr[i+1] <= 3 for i in range(len(arr) - 1))
        
        if is_increasing or is_decreasing:
            valid += 1
            continue
        
        for i in range(len(arr)):
            # Objetivo: pegar nos elementos anteriores e posteriores ao elemento atual
            # Exemplo: [10, 20, 30, 40, 50] -> [10, 20, 40, 50]
            modified_arr = arr[:i] + arr[i+1:]
            is_increasing = all(1 <= modified_arr[j+1] - modified_arr[j] <= 3 for j in range(len(modified_arr) - 1))
            is_decreasing = all(1 <= modified_arr[j] - modified_arr[j+1] <= 3 for j in range(len(modified_arr) - 1))
            
            if is_increasing or is_decreasing:
                valid += 1
                break
    print(valid)

challenge2()