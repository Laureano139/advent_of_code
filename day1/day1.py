
def dist():
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
        
    return distance

if __name__ == "__main__":
    print(dist())