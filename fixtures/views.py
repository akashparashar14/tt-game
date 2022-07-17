from django.shortcuts import render
import random

def highestPowerof2(n):
    res = 0
    for i in range(n, 0, -1):
        if ((i & (i - 1)) == 0):
            res = i
            break
    return res*2

team_size=int(input())

if team_size&1:
  up_half=(team_size+1)//2
  lw_half=(team_size-1)//2
else:
  up_half=(team_size)//2
  lw_half=(team_size)//2
byes=highestPowerof2(team_size)-team_size

print(up_half,lw_half,byes)

teams=[i for i in range(1,team_size+1)]

random.shuffle(teams)
print("Total teams=",teams)

round_2=teams[:byes]
print("Team got byes =",round_2)
match_teams=teams[byes:]
print("\n\n\nRound-1",match_teams)
j=0
print("\n\n------------Byes Tournament---------------")
for i in range(0,len(match_teams),2):
  print("Match Between",match_teams[j:i+2])
  winner=random.choice(match_teams[j:i+2])
  round_2.append(winner)
  print("Winner",winner,"\n")
  j=i+2
r=2
next_round=round_2
while True:
    j=0
    print("\n\n\nRound-"+str(r),round_2)
    for i in range(0,len(round_2)):
      match_btwn=round_2[j:i+2]
      if len(match_btwn)<=1:
        break
      print("Match Between",match_btwn)
      loser=random.choice(match_btwn)
      match_btwn.remove(loser)
      round_2.remove(loser)
      print("Winner",match_btwn[0],"\n")
      j=i+1
    r+=1
    if len(round_2)<=1:
      break