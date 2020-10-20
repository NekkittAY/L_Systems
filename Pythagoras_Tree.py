axiom = input() # axiom = 0
itr = int(input())
tempStr = ""
for i in range(1, itr+1):
    ln = len(axiom)
    for j in range(0,ln):
        if axiom[j] == "1":
            tempStr += "11"
        elif axiom[j] == "0":
            tempStr += "1[0]0"
        elif axiom [j] == "[":
            tempStr += "["
        else:
            tempStr += "]"
    axiom, tempStr = tempStr, ""
print(axiom)
