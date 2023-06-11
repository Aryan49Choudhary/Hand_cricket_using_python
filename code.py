import random
print("Time for toss \nodd or even")
toss = input()
n = random.randrange(1,7)
m = int(input())
print(n)
sum = n+m
commentary6 = ["What a shot!!","It\'s a huge one","Unbelievabe. Over the long-on fielder","In to the slot and it goes for a six","SIX! He never misses it from here","Yeh gend Melbourne jaakar giregi","Darshak bane fielder","Oochi toh gyi hai par kya door bhi...door hi yeh bahot door gyi hai","Ek baar fir bheja gend ko antariksh yatra pe"]
commentaryW = ["You miss I hit","Bowled him","What a catch","Edge and taken","LBW appeal and it\'s given","Direct hit","Hit-wicket. He will be highly dissapointed","Ballebaaj chaaro khaane chitt","It is up in the air and taken. What a catch","Gone at the slips"]
a=0
if sum%2==0:
    print("Even")
    if toss=='even':
        a=1
else:
    print("Odd")
    if toss=='odd':
        a=1
if a==1:
    print("You won the toss.")
    elect = input()
    print("and elected to",elect)
else:
    print("Opponent won the toss.")
    words = ("bat","ball")
    elect = random.choice(words)
    print("and elected to",elect)
if a==1:
    if elect=="bat":
        my = 0
        opp = 0
        c = 0
        b = 0
        while c!=2:
            turn = int(input())
            if (turn<1 or turn>6 and b==0):
                print("First Warning")
                b+=1
            elif (turn<1 or turn>6 and b!=0):
                print("out")
                print("Mankad")
                c+=1
            else:
                opp_turn = random.randrange(1,7)
                print(turn," , ",opp_turn)
                if (c==0):
                    if(turn!=opp_turn):
                        my+=turn
                        if (turn==6):
                            print(random.choice(commentary6))
                        print(my)
                    else:
                        c+=1
                        print("Out")
                        if my==0:
                            print ("Golden duck")
                        else:
                            print(random.choice(commentaryW))
                        print("Target of ",(my+1))
                else:
                    if (opp<=my and c==1):
                        if c==1:
                            if (turn!=opp_turn):
                                opp+=opp_turn
                                if opp_turn==6:
                                    print(random.choice(commentary6))
                                print(opp)
                            else:
                                c+=1
                                print("Out")
                                if opp==0:
                                    print ("Golden duck")
                                else:
                                    print(random.choice(commentaryW))
                                print("You win")
                    else:
                        print("Opponent wins")
    else:
        my = 0
        opp = 0
        c = 0
        b = 0
        while c!=2:
            turn = int(input())
            opp_turn = random.randrange(1,7)
            print(turn," , ",opp_turn)
            if (c==0):
                if (opp_turn!=turn):
                    opp+=opp_turn
                    if opp_turn==6:
                        print(random.choice(commentary6))
                    print(opp)
                else:
                    c+=1
                    print("OUT")
                    if opp==0:
                        print("Golden Duck")
                    else:
                        print(random.choice(commentaryW))
                    print("Target of ",(opp+1))
            else:
                if (turn<1 or turn>6 and b==0):
                    print("First Warning")
                    b+=1
                elif (turn<1 or turn>6 and b!=0):
                    print("out")
                    print("Mankad")
                    c+=1
                else:
                     my+=turn
                     if (my<=opp and c==1):
                        if c==1:
                            if (turn!=opp_turn):
                                if turn==6:
                                    print(random.choice(commentary6))
                                print(my)
                            else:
                                c+=1
                                print("Out")
                                print(random.choice(commentaryW))
                                print("Opponent wins")
                     else:
                         print("You win")
else:
    if elect=="ball":
        my = 0
        opp = 0
        c = 0
        b = 0
        while c!=2:
            turn = int(input())
            if (turn<1 or turn>6 and b==0):
                print("First Warning")
                b+=1
            elif (turn<1 or turn>6 and b!=0):
                print("out")
                print("Mankad")
                c+=1
            else:
                opp_turn = random.randrange(1,7)
                print(turn," , ",opp_turn)
                if (c==0):
                    if(turn!=opp_turn):
                        my+=turn
                        if (turn==6):
                            print(random.choice(commentary6))
                        print(my)
                    else:
                        c+=1
                        print("Out")
                        if my==0:
                            print ("Golden duck")
                        else:
                            print(random.choice(commentaryW))
                        print("Target of ",(my+1))
                else:
                    opp+=opp_turn
                    if (opp<=my and c==1):
                        if c==1:
                            if (turn!=opp_turn):
                                if opp_turn==6:
                                    print(random.choice(commentary6))
                                print(opp)
                            else:
                                c+=1
                                print("Out")
                                if opp==0:
                                    print ("Golden duck")
                                else:
                                    print(random.choice(commentaryW))
                                print("You win")
                    else:
                        print("Opponent wins")
    else:
        my = 0
        opp = 0
        c = 0
        b = 0
        while c!=2:
            turn = int(input())
            opp_turn = random.randrange(1,7)
            print(turn," , ",opp_turn)
            if (c==0):
                if (opp_turn!=turn):
                    opp+=opp_turn
                    if opp_turn==6:
                        print(random.choice(commentary6))
                    print(opp)
                else:
                    c+=1
                    print("OUT")
                    if opp==0:
                        print("Golden Duck")
                    else:
                        print(random.choice(commentaryW))
                    print("Target of ",(opp+1))
            else:
                if (turn<1 or turn>6 and b==0):
                    print("First Warning")
                    b+=1
                elif (turn<1 or turn>6 and b!=0):
                    print("out")
                    print("Mankad")
                    c+=1
                else:
                     my+=turn
                     if (my<=opp and c==1):
                        if c==1:
                            if (turn!=opp_turn):
                                if turn==6:
                                    print(random.choice(commentary6))
                                print(my)
                            else:
                                c+=1
                                print("Out")
                                print(random.choice(commentaryW))
                                print("Opponent wins")
                     else:
                         print("You win")
