print("Multiplication table")
#display the number title
print("|",end=" ")
for j in range(1,11):
    print(" ",j,end=" ")
print() #jump to the new line
print("-----------------------------------")

#display table body
for i in range(1,11):
      print(i,"|",end=" ")
      for j in range(1,11):
          print(format(i*j,"4d"),end=" ")
      print() #jump to the new line
      
      
