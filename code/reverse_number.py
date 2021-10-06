#REVERSE GIVEN NUMBER
#GITHUB:dharmateja03
number=int(input())   #enter input
if number>=0:
  s=str(number)         #converting into string
  ans=s[::-1]
  print(ans)
else:
  number=-1*number
  s=str(number)         #converting into string
  ans=s[::-1]
  print("-"+ans)
  
