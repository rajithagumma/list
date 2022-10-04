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
while i<len(questions_list):
    print(questions_list[i])
    print("1.",options_list[i][0])
    print("2.",options_list[i][1])
    print("3.",options_list[i][2])
    print("4.",options_list[i][3])
    answer=int(input("enter your answer"))
    if answer==solutions_list[i]:
        print("congraslations your answer is correct")
    elif answer!=solutions_list:
        print("your answer is wrong")
        break
    i=i+1
i=0