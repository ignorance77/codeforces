n = int(raw_input())
for i in range(0, n) :
    s = raw_input()
    lastalpha = 0
    firstdigit = -1
    for j in range(0, len(s)) :
        if (s[j].isdigit() and firstdigit == -1) :
            firstdigit = j
        if (s[j].isalpha()) :
            lastalpha = j
    if (firstdigit < lastalpha) :
        k = s.index("C");
        x = int(s[1:k])
        y = int(s[(k + 1):])
        sx = ""
        while (y > 0) :
            c = (y % 26) - 1
            if (c < 0) :
                c = 25
            sx = sx + chr(ord('A') + c);
            y /= 26
        print sx[::-1] + str(x)
    else :
        j = 0
        part1 = ""
        part2 = ""
        total = 0
        while (s[j].isalpha()) :
            part1 += s[j]
            total = total * 26 + (ord(s[j]) - ord('A') + 1);
            j = j + 1
        while (j < len(s)) :
            part2 += s[j]
            j = j + 1
        ret = 'R' + part2 + 'C' + str(total);
        print ret;
