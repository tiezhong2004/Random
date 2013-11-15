
units = "mm"

lengthoftimber= 5400
availablelengths = 8
contingency = 90

requiredlengths = [2603,
2603, #(5206)

1498, 
1498, #(2996)  

1175, 
1175, #(2350)

990,
990, #(1980)

1325, 
1325, #(2650)

2840, 
2840, #(5680) 

1890,
1890, #(3780)

1328,
1328, #(2656) 

1177,
1177, #(2345)

1150,
1150, #(2300)

1648,
1648, #(3296)

984,
984, #(1968)

462,
462, #(924)

645,
645,] #(1290)


print "Lengths required", len(requiredlengths)


def sumBucket(buck):
    adder = 0
    for n in buck:
        adder += n 

    return adder

newlengths = []
# Adjust for window trim
for u in requiredlengths:
    newlengths.append(u + contingency)

l = sorted(newlengths, reverse=True)

buckets = []

# Assign long lengths to buckets
for i in range(0, availablelengths):
    buckets.append([l[i]])
    
# Remove lengths from list
l = l [8:]

# For each bucket find remainder and find next longest
for o in range(0, len(l)):
    for k in buckets:
        rem = lengthoftimber - sumBucket(k)

        for j in l:
            if j <= rem:
                k.append(j)
                l.remove(j)
                break


print "Remainging lengths", len(l)

for i, p in enumerate(buckets):
    print "Length", i+1, "cuts:", p, " Remainder:", lengthoftimber - sumBucket(p), units


