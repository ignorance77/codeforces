n = int(raw_input())

final = {}
scores = []
names = []

for i in range(0, n) :
    name, score = raw_input().split()
    total = final.get(name, 0) + int(score)
    final[name] = total
    names.append(name)
    scores.append(score)

best = -1;

for name in final :
    score = final.get(name);
    if ( score > best ) :
        best = score

values = {}

for i in range (0, n) :
    total = values.get(names[i], 0) + int(scores[i])
    values[names[i]] = total
    if (total >= best and final[names[i]] == best) :
        winner = names[i]
        break

print winner
