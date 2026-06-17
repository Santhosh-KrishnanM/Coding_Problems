n, m = [int(x) for x in input().split()]
a = [int(y) for y in input().split()][:n]
b = [int(z) for z in input().split()][:m]
c = 0
s1,s2 = set(),set()
for i in range(0,n):
    l = a[i]
    for j in range(0,m):
        if b[j] <= 2 * l and j not in s2 and i not in s1:
            s1.add(i)
            s2.add(j)
            c += 1
print(c)