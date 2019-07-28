import random

score1=0
score2=0
i=1
def bat(x,y):
    if x==1:
        while i!=0:
            bat=int(input("Enter a no"))
            bowl=random.randint(0,10)
            if bat==bowl:
             if y==0:
              print('You are out')
              break
             else:
                 bowl(1,0)
                 break
             score1+=bat
    else:
        while i!=0:
            bat=random.randint(1,10)
            bowl=int(input('Enter bowling no'))
            if bat==bowl:
                if y==0:
                    print('the opponent died')
                    break
                else:
                    bowl(0,0)
                    score1+=bat

def bowl(x,y):
    if x==1:
        while i!=0:
            bowl=int(input("Enter a no"))
            bat=random.randint(0,10)
            if bat==bowl:
             if y==0:
              print('You are out')
              break
             else:
                 bowl(1,0)
                 break
             score1+=bat
    else:
        while i!=0:
            bowl=random.randint(1,10)
            bat=int(input('Enter bowling no'))
            if bat==bowl:
                if y==0:
                    print('the opponent died')
                    break
                else:
                    bat(0,0)
                    score1+=bat




print('Welcome to handcricet ')

print('Toss:\n1 for heads\n2 for Tails ')
n=int(input('Enter ur toss:'))
m=random.randint(1,2)
if n==m:
    print('u won the toss')
    print('Enter\n1 for batting\n2 for bowling ')
    l=int(input("Enter ur choice:"))
    if l==1:
        bat(1,1)
    else:
        bowl(1,1)
else:
    print('U lost the toss ')
    b=random.randint(1,2)
    if b==1:
        print('The opponent chose batting')
        bat(0,1)
    else:
        bowl(0,1)