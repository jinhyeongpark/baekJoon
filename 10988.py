word = input()
is_pal = True
for i in range(int(len(word)/2)):
    if word[i] != word[-i-1]:
        is_pal = False
        break
if is_pal:
    print(1)
else:
    print(0)