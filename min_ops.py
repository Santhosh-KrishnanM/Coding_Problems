def repl(s,t,c):
    n = len(s)
    for i in range(n):
        if s[i] != t[i]:
            s.replace(s[i],t[i],1)
            c += 1
    return c
    
def ins(s,t,c):
    n = len(s)
    for i in range(n):
        if s[i] != t[i]:
            ns = s[:i] + t[i] + s[i:]
            c += 1
            if ns == t:
                return c
            
    print(ns)
    return c

def rem(s,t,c):
    n = len(t)
    for i in range(n):
        if s[i] != t[i]:
            ns = s[:i] + s[i+1:]
            c += 1
            if ns == t:
                print(ns)
                return c
    return c

s = input()
t = input()
c = 0
print(f"s = {s}  t = {t}")
if len(s) == len(t):
    print(repl(s,t,c))
elif len(s) < len(t):
    print(ins(s,t,c))
elif len(s) > len(t):
    print(rem(s,t,c))
