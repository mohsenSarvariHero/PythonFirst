def readList(list1):
  while True : 
      user = int(input("enter number: "))
      if(user < 0 ):
          break
      if user not in list1:
          list1.append(user)
  return list1


def printList(list1):
    for i in list1:
         if(type(i)== list):
            printList(i)
         else:
            print(i , end=" ")
    print()
    

def delindex(list , index):
    del list[index]
    
    
    
def func1():
    for i in range(1,12):
        if(i%2==0):
            print("__",end="")
        else:
            print("**",end="")
    print()
    return 'the End'




def fibo(limit):
    a = 1 
    b = 1
    list1=[1,1]
    i = 0
    while(i<limit):
        c = a+b
        list1.append(c)
        a = b
        b = c
        i +=1
    return(list1)


def factoriel(num):
    if(num == 0 or num ==1):
        return 1
    result = num * factoriel(num-1)
    return result




def sunl(list2):
    list3=[]
    for i in range(0,len(list2)+1):
        for j in range(0,i):
            list3.append(list2[j:i])
    return list3