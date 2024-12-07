
def challenge1():
    arr1 = []
    arr2 = []
    
    with open("input.txt") as file:
        for line in file:
            n1, n2 = line.split()
            arr1.append(int(n1))
            arr2.append(int(n2))
            
    list1 = sorted(arr1)
    list2 = sorted(arr2)
    
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    print(f"Resultado C1: {distance}\n")
    return distance

challenge1()

def challenge2():
    
    arr1 = []
    arr2 = []
    
    with open('input2.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            n1, n2 = line.split()
            arr1.append(int(n1))
            arr2.append(int(n2))
        
        total_similarity = 0
        for num1 in arr1:
            counter = 0
            for num2 in arr2:
                if num1 == num2:
                    counter += 1
            if counter == 0:
                continue
            else:
                similarity = num1 * counter
            total_similarity += similarity
        print(f"Resultado C2: {total_similarity}\n")
        return total_similarity
    
challenge2()