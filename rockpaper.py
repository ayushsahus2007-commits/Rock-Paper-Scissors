import random as r
Cch=r.randint(1,3)
# 1=rock
# 2=paper
# 3=scissors
print("Welcome to rock, paper, scissors game.")
print("1.Rock")
print("2.Scissors")
print("3.Paper")
while True:
    Uch=int(input("Enter your choice: "))
    print("Computer choice was:",Cch)
    if Uch==Cch:
        print("Draw")
    elif Uch==2 and Cch==3:
        print("Win")
    elif Uch==1 and Cch==3:
        print("Loss")
    elif Uch==2 and Cch==1:
        print("Win")
    elif Uch==3 and Cch==1:
        print("Loss")
    elif Uch==1 and Cch==2:
        print("Win")
    elif Uch==3 and Cch==2:
        print("Loss")
    ch=input("More(Y/N):")
    if ch in 'Nn':
        break