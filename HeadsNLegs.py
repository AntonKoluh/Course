Heads = int(input("Heads: "))
Legs = int(input("Legs: "))

Parts = (Heads, Legs)
Cows = int(Parts[1]/2 - Parts[0])
Results = (Cows, abs(Parts[0] - Cows))
checkParts = ((Results[0]+Results[1]), (Results[0]*4 + Results[1]*2))

if (checkParts[0] - Parts[0]) or (checkParts[1] - Parts[1]) is not 0:
    print ("Impossible")
else:
    print(f"(Cow, Chicken): {Results}")
