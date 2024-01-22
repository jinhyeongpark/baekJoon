MatList = [list(map(int, input().split())) for _ in range(9)]

maxList = [max(row) for row in MatList]
overallMax = max(maxList)

rowIndex = maxList.index(overallMax)
columnIndex = MatList[rowIndex].index(overallMax)

print(overallMax)
print(rowIndex + 1, columnIndex + 1)

    