def fun(a,b):
          if a>b:
                    return a
          else:
                    return b
def fun1(a,b):
          print(fun(a,b))
          print(a+b)
fun1(12,13)

def greater(a,b):
          if a>b:
                    return a
          else:
                    return b
def greatest(a,b,c):
          if greater(a,b)>c:
                    return greater(a,b)
          else:
                    return c
print(greatest(12,10,19))


def disp():
          def show():
                    return "show function"
          print("disp function")
          return show
