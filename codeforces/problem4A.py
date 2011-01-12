n = int(raw_input())
i = 0
good = 0
while i <= n :
    i += 2
    j = 0
    while j <= n :
        j += 2
        if (i + j == n) :
            good = 1
if (good) :
    print "YES"
else :
    print "NO"