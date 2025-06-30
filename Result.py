#result for the five main subjets
#variable as subject name 
english=int(input("enter the number obtained in english subject:  "))
hindi=int(input("enter the number obtained in hindi subject:  "))
science=int(input("enter the number obtained in science subject:  "))
maths=int(input("enter the number obtained in maths subject:   "))
socialscience =int(input("enter the number obtained in social science :  "))
list1=[]
list1.append(english)
list1.append(hindi)
list1.append(science)
list1.append(maths)
list1.append(socialscience)
result=sum(list1)
print ("Result :",result)
if (result >=430):
  print("Division 1")
elif (result >=300):
  print("Division 2")
elif (result >=200):
  print ("Division 3")
else print("Fail")  

