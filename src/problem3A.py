start = raw_input()
end = raw_input()

startx = ord(start[0]) - ord('a')
starty = ord(start[1]) - ord('1')

endx = ord(end[0]) - ord('a')
endy = ord(end[1]) - ord('1')

di = [-1, 0, 1, 1, 1, 0, -1, -1 ] ;
dj = [ -1, -1, -1, 0, 1, 1, 1, 0] ;
cc = [ 'LD', 'L', 'LU', 'U', 'RU', 'R', 'RD', 'D' ];

curi = starty;
curj = startx;

path = []

while (1) :
    best = abs(endx - curj) + abs(endy - curi)
    bk = -1
    for k in range(0, 8) :
        ni = curi + di[k]
        nj = curj + dj[k]
        if (ni >= 0 and nj >= 0 and ni < 8 and nj < 8) :
            diff = abs(endx - nj) + abs(endy - ni)
            if (diff < best) :
                best = diff
                bk = k
    if (bk == -1) :
        break
    curi += di[bk]
    curj += dj[bk]
    path.append(cc[bk])

print len(path)
for i in range(0, len(path)) :
    print path[i]