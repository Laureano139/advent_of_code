import re

def challenge1():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        
        rString = r"mul[(](\d+),(\d+)[)]"
        
        somaMul = 0
        
        for line in data:
            matches = re.findall(rString, line)
            for match in matches:
                num1, num2 = map(int, match)
                somaMul += num1 * num2
                
    print(f"Resultado C1: {somaMul}\n")
    return somaMul
        
challenge1()

def challenge2():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        
        rString = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
        
        somaMul = 0
        
        megaString = "".join(data)
            
        mulOperation = True
        
        instructions = re.findall(rString, megaString)
        
        for instr in instructions:
            if instr[0] == "don't()":
                mulOperation = False
            elif instr[0] == "do()":
                mulOperation = True
            elif instr[1] and instr[2]:
                if mulOperation:
                    num1, num2 = int(instr[1]), int(instr[2])
                    somaMul += num1 * num2
                
    print(f"Resultado C2: {somaMul}\n")
    return somaMul
        
challenge2()