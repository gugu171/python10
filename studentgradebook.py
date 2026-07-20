scores = {'Jennifer': 1, 'Johnny': 10, 'Bobina': 0, 'Bobby': 23, 'Bingbong': 100}
totalscore = 0
for student in scores:
    totalscore += scores[student]

avg = totalscore / len(scores)
min_scorer = min(scores, key=scores.get)
max_scorer = max(scores, key=scores.get)

print("----- CLASS GRADE BOOK -----")
print("AVERAGE SCORE =",avg,'marks')
print('HIGHEST SCORER:',max_scorer,)
print('LOWEST SCORER:',min_scorer)
print('----------------------------')

searchperson = input('Enter a person you want to search up: ') #choose from 'Jennifer, Johnny, Bobina, Bobby and Bingbong'
searchgrade = scores.get(searchperson, 'Student not found :(')

print("Result:",searchgrade,'marks')