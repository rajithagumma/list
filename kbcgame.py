print("WELCOME TO KBC GAME")
name=input("enter your name")
questions_list=["how many schedules are there indian constitution","father of local governments in india",
"who is the first women president indian national congress","where is the international rice research centre"]
options_list=[["Eight","ten","twelve","nine"],["Lorddafrin","Lord litton","waren hasting","Lord rippon"],
["Annie Bessant","Sarojini naidu","Indira gandhi","prathiba patel"],
["kotak","Manila","The Hague ","India"]]
solutions_list=[3,4,1,2]
fifty_options=[["Eight","twelve"],["warenhasting","lord rippon"],["annie besant","Indhira gandhi"],
["manila","india"]]
fifty_solutions=[2,2,1,1]
i=0
fifty=0
while i<1:
    print(questions_list[i])
    print("1.",options_list[0][0])
    print("2.",options_list[0][1])
    print("3.",options_list[0][2])
    print("4.",options_list[0][3])
    print("1.with lifeline, 2.without lifeline")
    choice=int(input("enter ur option"))
    if choice==1:
        fifty+=1
        print("1.",fifty_options[0][0])
        print("2.",fifty_options[0][1])
        answer=int(input("enter your answer:"))
        if answer==fifty_solutions[0]:
            print("congratslations your answer is correct")
            print("you won 5000 rupees")
        else:
            print("your answer is wrong")
            print("better luck for next time")
            break
    if choice==2:
        answer=int(input("enter your answer:"))
        if answer==solutions_list[0]:
            print("congraslations you won 10,000 rupees")
        else:
            print("oops wrong answer")
            break
    i=i+1
i=0
while i<1:
    print(questions_list[1])
    print("1.",options_list[1][0])
    print("2.",options_list[1][1])
    print("3.",options_list[1][2])
    print("4.",options_list[1][3])
    print("1.with lifeline, 2.without lifeline")
    choice=int(input("enter ur option"))
    if choice==1:
        fifty+=1
        if fifty==0:
            print("1.",fifty_options[1][0])
            print("2.",fifty_options[1][1])
            answer=int(input("enter your answer:"))
            if answer==fifty_solutions[1]:
                print("congratslations your answer is correct")
                print("you won 5000 rupees")
            else:
                print("your answer is wrong")
                print("better luck for next time")
                break
        else:
            print("you already used your 5050 lifeline")
    if choice==2:
        answer=int(input("enter your answer:"))
        if answer==solutions_list[1]:
            print("congraslations you won 10,000 rupees")
        else:
            print("oops wrong answer")
            break
    i=i+1
i=0
while i<1:
    print(questions_list[2])
    print("1.",options_list[2][0])
    print("2.",options_list[2][1])
    print("3.",options_list[2][2])
    print("4.",options_list[2][3])
    print("1.with lifeline, 2.without lifeline")
    choice=int(input("enter ur option"))
    if choice==1:
        fifty+=1
        if fifty==0:
            print("1.",fifty_options[2][0])
            print("2.",fifty_options[2][1])
            answer=int(input("enter your answer:"))
            if answer==fifty_solutions[2]:
                print("congratslations your answer is correct")
                print("you won 25000 rupees")
            else:
                print("your answer is wrong")
                print("better luck for next time")
                break
        else:
            print("you already used your 5050 lifeline")
    if choice==2:
        answer=int(input("enter your answer:"))
        if answer==solutions_list[2]:
            print("congraslations you won 10,000 rupees")
        else:
            print("oops wrong answer")
            break
    i=i+1
i=0
while i<1:
    print(questions_list[3])
    print("1.",options_list[3][0])
    print("2.",options_list[3][1])
    print("3.",options_list[3][2])
    print("4.",options_list[3][3])
    print("1.with lifeline, 2.without lifeline")
    choice=int(input("enter ur option"))
    if choice==1:
        fifty+=1
        if fifty==0:
            print("1.",fifty_options[3][0])
            print("2.",fifty_options[3][1])
            answer=int(input("enter your answer:"))
            if answer==fifty_solutions[3]:
                print("congratslations your answer is correct")
                print("you won 50000 rupees")
            else:
                print("your answer is wrong")
                print("better luck for next time")
                break
        else:
            print("you already used your 5050 lifeline")
    if choice==2:
        answer=int(input("enter your answer:"))
        if answer==solutions_list[3]:
            print("congraslations you won 10000000 rupees")
        else:
            print("oops next time better luck")
            break
    i=i+1





        




        



