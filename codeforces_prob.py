t = int(input())
l = []
for _ in range(t):
    n =  int(input())
    g = []
    for i in range(n):
        g = [int(x) for x in input().split()][:n]
        sg = sorted(g)
        d = 0
        if sg == g:
            l.append("Yes")
            break
        for x in range(n):
            for x in range(n - 1):
                if g[x] > g[x+1]:
                    g[x], g[x+1] = g[x+1], g[x]
                    d += 1
        if d > 1:
            l.append("No")
            break
        else:
            l.append("Yes")
            break
print()
for i in l:
    print(i)
