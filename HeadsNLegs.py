Heads = int(input("Enter Heads: "))
Legs = int(input("Enter Legs: "))

Parts = (Heads, Legs)
Cows = int(Parts[1]/2 - Parts[0])
Results = (abs(Cows), abs(Parts[0] - Cows))
checkParts = ((Results[0] + Results[1]), (Results[0]*4 + Results[1]*2))

if Parts == checkParts:
    print(f"(Cow, Chicken): {Results}")
else:
    print ("Impossible")
