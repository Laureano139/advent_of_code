import re

def mulRes():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        
        rString = r"mul[(](\d+),(\d+)[)]"
        
        somaMul = 0
        
        for line in data:
            match = re.search(rString, line)
            if match:
                num1 = match.group(1)
                num2 = match.group(2)
                print(f"Número 1: {num1}, Número 2: {num2}\n")
                somaMul += int(num1) * int(num2)
                
    print(f"Soma dos resultados das multiplicações: {somaMul}")
        
mulRes()