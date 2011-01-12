
def isTriangle (a, b, c):
    return (a + b > c and a + c > b and b + c > a);

def isSegment (a, b, c):
    return (a + b >= c and a + c >= b and b + c >= a);

L = raw_input().split()
triangle = False
segment = False

for i in range(0, 4) :
    for j in range(0, 4) :
        for k in range(0, 4) :
            if (i != j and j != k and i != k) :
                triangle |= isTriangle(int(L[i]), int(L[j]), int(L[k]))
                segment |= isSegment(int(L[i]), int(L[j]), int(L[k]))

if (triangle) :
    print "TRIANGLE"
else :
    if (segment) :
        print "SEGMENT"
    else :
        print "IMPOSSIBLE"