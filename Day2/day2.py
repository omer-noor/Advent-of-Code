file1 = open('day2input.txt', 'r')
Lines = file1.readlines()  

scores = {'X':1,'Y':2,'Z':3}

matchups = {'X':'C','Y':'A','Z':'B'}
matchups2 = {'A':'Y','B':'Z','C':'X'}

conversions= {'A':'X','B':'Y','C':'Z'}

totalScore=0

for line in Lines:
    roundScore=0
    chars=(line.strip().split())
    opponent=chars[0]
    player=chars[1]    

    if matchups[player]==opponent:
        roundScore+=6    
    if conversions[opponent]==player:
        roundScore+=3    
    
    roundScore+=scores[player]
    totalScore+=roundScore

print(totalScore)

totalScore=0

for line in Lines:
    roundScore=0
    chars=(line.strip().split())
    opponent=chars[0]
    result=chars[1]

    if result=='X':        
        roundScore+=scores[conversions[matchups[conversions[opponent]]]]
    elif result=="Y":
        roundScore+=scores[conversions[opponent]]+3
    else:
        roundScore+=scores[matchups2[opponent]]+6
    
    totalScore+=roundScore

print(totalScore)




