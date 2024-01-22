words = [list(input()) for _ in range(5)]
rep = max([len(word) for word in words])

for i in range(rep):
    for j in range(5):
        try:
            print(words[j][i], end="")
        except IndexError:
            pass
