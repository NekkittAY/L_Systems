axiom = input() # axiom = F
itr = int(input())
tempStr = ""
for i in range(1, itr+1):
    ln = len(axiom)    
    for j in range(0, ln):
        if axiom[j] == "+":
            tempStr += "+"
        elif axiom[j] == "-":
            tempStr += "-"
        else:
            tempStr += "F+F-F-F+F"
    axiom, tempStr = tempStr, ""
print(axiom)
