def lucky_no(cn):
    if cn <= 0 or cn < 1000 or cn > 10000:
        print(f"{cn} is not a valid car number")
        return
    r = 0
    while cn > 0:
        t = cn % 10
        r += t
        cn //= 10
    
    s = 1 if r % 3 == 0 or r % 5 == 0 or r % 7 == 0 else 0
    if s:
        print(f"Lucky Number")
    else:
        print(f"Sorry its not my lucky number")
cn = int(input())
lucky_no(cn)
