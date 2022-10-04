print("WELCOME TO KBC GAME")
name=input("enter your name")
questions_list=["1.how many schedules are there indian constitution","2.father of local governments in india",
"3.who is the first women president indian national congress","4.where is the international rice research centre"]
options_list=[["1.Eight","2.ten","3.twelve","4.nine"],["1.Lorddafrin","2.Lord litton","3.waren hasting","4.Lord rippon"],
["1.Annie Bessant","2.Sarojini naidu","3.Indira gandhi","4.prathiba patel"],
["1.kotak","2.Manila","3.The Hague ","4.India"]]
solutions_list=[3,4,1,2]
fifty_options=[["1.Eight","2.twelve"],["1.warenhasting","2.lord rippon"],["1.annie besant","2.Indhira gandhi"],
["1.manila","2.india"]]
fifty_solutions=[2,2,1,1]
price=[" WONNERFUL ANSWER!YOU WON 1000 RUPEES","CONGRASLATIONS","WOW!GREAT ANSWER","AWESOME,YOU ARE WINNER KBC GAME"]
eliminate=["OOPS YOUR ANSWER IS WRONG","NEXT TIME BETTER LUCK","YOU LOSS THE GAME","PREPARE WELL FOR NEXT GAME"]
i=0
index=0
count=0
while i<len(questions_list):
    c=questions_list[i]
    print(c)
    j=0
    while j<len(options_list):
        n=options_list[i][j]
        j=j+1
        print(n)
    print("1.with lifeline")
    print("2.without lifeline")
    choose=int(input("enter the your choice:"))
    if choose==1:
        if count==0:
            z=0
            while z<len(fifty_options):
                d=fifty_options[i]
                z=z+1
            print(d)
            count=count+1
            choice=int(input("enter your answer:"))
            if choice==fifty_solutions[index]:
                print(price[i])
            else:
                print(eliminate[i])
                break
        else:
            print("you already used ur 5050 lifeline")
            choice=int(input("enter your choice"))
            if choice==solutions_list[index]:
                print(price[i])
            else:
                print(eliminate[i])
                break
    else:
        choice=int(input("enter your answer:"))
        if choice==solutions_list[index]:
            print(price[i])
        else:
            print(eliminate[i])
            break
    index=index+1
    i=i+1  