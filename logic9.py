a=input("enter the number:")
b=int(a[0:3])
c=int(a[3:6])
d=int(a[6:10])
if len(a)==10:
    if b>=100 and b<=999:
        if c>=100 and c<=999:   
            if d>=1000 and c<=9999:
                print("("+str(b)+")"+"-"+str(c)+"-"+str(d))
            else:
                print("nothing1")
        else:
            print("nothing1")
    else:
        print("nothing3")
else:
    print("nothing3")