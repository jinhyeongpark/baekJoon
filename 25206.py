#전공평점 = (학점 * 과목평점) / 학점 총합
#P/F에서 P의 경우 계산에서 제외
scoreForlec = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
scores = 0
scoreNum = 0
for i in range(20): 
    lecture, score, grade = input().split()
    if grade == 'P':
        continue
    grade = scoreForlec[grade]
    scores += float(score) * float(grade)
    scoreNum += float(score)

print(round((scores/scoreNum), 6))

