s = input()

start = 0
dic_char = {}
max_len = 0
bs = 0
for end in range(len(s)):
    cur_char = s[end]
    if cur_char in dic_char and dic_char[cur_char] >= start:
        start = dic_char[cur_char] + 1
    dic_char[cur_char] = end
    cur_len = end - start + 1
    if cur_len > max_len:
        max_len = cur_len
        bs = start
print(s[bs:bs+max_len])
