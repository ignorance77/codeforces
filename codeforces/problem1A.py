n, m, a = raw_input().split()
n = int(n)
m = int(m)
a = int(a)
if (n % a != 0) :
    n += (a - (n % a))
if (m % a != 0) :
    m += (a - (m % a))
ret = (n * m) / (a * a);
print ret