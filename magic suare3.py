a=[[8,3,4],
   [1,5,9],
   [6,7,2]]
i=0
while i<len(a):
   fr=0
   sr=0
   tr=0
   fc=0
   sc=0
   tc=0
   dia1=0
   dia2=0
   k=len(a)-1
   j=0
   while j<len(a):
      fr+=a[0][j]
      fc+=a[j][0]
      sr+=a[1][j]
      sc+=a[j][1]
      tr+=a[2][j]
      tc+=a[j][2]
      dia1+=a[j][j]
      dia2+=a[k][j]
      j=j+1
   i=i+1
   k=k-1
print("first row",fr)
print("second row",sr)
print("third row",tr)
print("first column",fc)
print("second column",sc)
print("third column",tc)
print("diagonal1",dia1)
print("diagonal2",dia2)
if fr==sr==tr==fc==sc==tc==dia1==dia2:
   print(a,"is amagic square")
else:
   print(a,"not a magic square")