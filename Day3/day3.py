result=0

with open('Day3\day3input.txt') as file:
  for line in file:
    #do stuff to each line in the file
    line=line.strip()
    leftSet, rightSet= set(), set()
    left, right = 0, len(line)-1
    while left<right:                 
      leftSet.add(line[left])
      rightSet.add(line[right])
      left+=1
      right-=1
    res=leftSet.intersection(rightSet)

    for r in res:      
      if r.isupper():
        result+=ord(r)-64+26
      else:
        result+=ord(r)-96
file.close()

print(result)

with open('Day3\day3input.txt') as file:
  result=0
  counter=0  
  setList=[]
  for line in file:
    counter+=1
    line=line.strip()
    curr=set(line)
    setList.append(curr)
    if counter==3:
      inter = setList[0].intersection(setList[1].intersection(setList[2]))
      r=inter.pop()
      if r.isupper():
        result+=ord(r)-64+26
      else:
        result+=ord(r)-96
      counter=0
      setList=[]
  print(result)
    
    
    
    



