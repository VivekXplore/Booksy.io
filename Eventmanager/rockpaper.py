
'''
rock=1
paper=-1
scissor=0

'''



import random 

dictionari={
    1:"rock",
    -1:"paper",
     0:"scissor"
}

you = int(input("Enter your choice (rock, paper, scissor): "))

user_input=dictionari[you]

if you not in dictionari:
    print("invalid choice selected ")
else:
    user_input= you
    print(f"Your choice: {dictionari[user_input]}")



computer=random.randint(1,1)
print(f"Computer's choice: {dictionari[computer]}")


if(user_input==1 and computer==-1):
    print("you lose ")

elif(user_input==-1 and computer== 0):
    print("you loose ")

elif(user_input==0 and computer==1 ):
    print('you loose ')

elif(user_input==-1 and computer==1):
    print("you win")




elif(user_input==1 and computer==0):
    print("you win")

elif(user_input==0 and computer==-1):
    print("you win")

elif(user_input==1 and computer==1):
    print("draw")

elif(user_input==0 and computer==0):
    print("draw ")

elif(user_input==-1 and computer==-1):
    print("draw ")

else:
    print("something went wrong ")