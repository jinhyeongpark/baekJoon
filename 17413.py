import sys

input = sys.stdin.readline

arr = input().strip()
flag = True
words = ""
res = ""

for word in arr:
    words += word
    if word == "<":
        flag = False
    if word == ">":
        res += words
        words = ""
    elif len(words) > 1 and word == "<":
        res += words[:-1][::-1]
        words = "<"
    elif word == " ":
        if flag == True:
            res += (words.strip())[::-1] + " "
            words = ""
        flag = True
res += words[::-1]
print(res)