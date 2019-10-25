
#Get input from the user for no: of rounds
rounds = int(input("No of rounds to play "))

#setting scores values
scores={"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}

bonuscheck=[]
bonusplayer=[]

# Given the players list w r t its team with  initial score zero

teams={"Gyrhuna":[{"Jaons Dain":0},{"Susu":0}],
       "Achni":[{"Milog":0},{"Tianlong":0}],
       "Bathar":[{"Pakhangba":0},{"Poubi Lai Paphal":0}]}

teamno=len (teams)
bonusteam={}
teamscore={}
def whowonthematch(teamscore):
    return [key  for (key, value) in teamscore.items() if value == max(teamscore.values())]


for team in teams:
    bonusteam[team]=0
    teamscore[team]=0
players=0
for i in teams:
    players+=len(teams[i])


playerscores={}

for r in range(rounds):
    for team in teams:
        #print(team)

        bonuscheck=[]
        bonusplayer=[]
        teamscore[team]=0
        for pl in teams[team]:
            key, value = list(pl.items())[0]
            #print(key)
            temp=0
            playerscore=(input("Enter the score of " +str(key)+str(" from team ")+team+" "))
            if playerscore not in (["A","B","C","D","E","F"]):
                print("Please select the score from A-F")
                exit(0)
            bonuscheck.append(playerscore)
            bonusplayer.append(key)
            prefix=key
            if prefix  not in  playerscores:

                playerscores[prefix]=scores[playerscore]
                #print(playerscores[prefix])
            else:
                playerscores[prefix]+=scores[playerscore]
                temp=playerscores[prefix]
            teamscore[team]+=playerscores[prefix]

        if(len(set(bonuscheck))==1):
            #print("has bonus")
            bonusteam[team]+=2
        teamscore[team]+=bonusteam[team]

    scores={key:value+1 if(key!="F") else value  for key,value in(scores.items()) }

    print(playerscores)
    print(bonusteam)
    print(teamscore)
    print("Next Round")

key=whowonthematch(teamscore)[0]
print("Game over. {} won!!!".format(key))






