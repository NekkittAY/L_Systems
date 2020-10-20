axiom = input() # axiom = A
itr = int(input())
tempStr = ""
for i in range(1, itr+1):
    ln = len(axiom)
    for j in range(0, ln):
        if axiom[j] == "A":
            tempStr += "B-A-B"
        elif axiom[j] == "B":
            tempStr += "A+B+A"
        elif axiom[j] == "+":
            tempStr += "+"
        elif axiom[j] =="-":
            tempStr += "-"
    axiom, tempStr = tempStr, ""
print(axiom)
