
units = "mm"

lengthoftimber= 5400
availablelengths = 3
contingency = 90

requiredlengths = [
2900,
2900,
1960,
1960,
1400,
1400,
1400,
1400

]


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
l = l [availablelengths:]

# For each bucket find remainder and find next longest
for o in range(0, len(l)):
    for k in buckets:
        rem = lengthoftimber - sumBucket(k)

        for j in l:
            if j <= rem:
                k.append(j)
                l.remove(j)
                break




for i, p in enumerate(buckets):
    print "Length", i+1, "cuts:", p, " Remainder:", lengthoftimber - sumBucket(p), units

print "Remainging lengths", len(l)

